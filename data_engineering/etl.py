from msc.util import *
from orm.model import *
from orm import create_db, Session
import pandas as pd
from sqlalchemy import inspect

def base_read(path):

    df = pd.read_csv(path, parse_dates=True, dayfirst=True)

    return df

def base_load(df, Table, column_map, session):

    table_map = inspect(Table)

    column_name = [column.name for column in table_map.columns]
    primary_key = [key.name for key in table_map.primary_key]

    df = df.rename(columns=column_map)
    df = df[column_name]
    df = df.drop_duplicates(subset=primary_key)
    df = df.set_index(keys=primary_key)

    for idx, row in df.iterrows():

        if type(idx) != tuple:
            idx = [idx]
        else:
            idx = list(idx)

        pks = dict(zip(primary_key,idx))
        idx.extend(row)
        cls = dict(zip(column_name,idx))

        query = session.query(Table).filter_by(**pks)

        if not session.query(query.exists()).scalar():
            table_instance = Table(**cls)
            session.add(table_instance)
        else:
            pass

    print('Commit na tabela: {0}'.format(Table.__tablename__))
    session.commit()

def main():

    price_quote = base_read(PATHS['price_quote'])
    price_quote = convert_boolean(price_quote, ['bracket_pricing'])
    price_quote = convert_datetime(price_quote, ['quote_date'])

    base_load(price_quote, Supplier, COLUMNS_MAP['supplier'], session)
    base_load(price_quote, TubeAssembly, COLUMNS_MAP['tube_assembly'], session)
    base_load(price_quote, PriceQuote, COLUMNS_MAP['price_quote'], session)

    comp_boss = base_read(PATHS['component_boss'])
    comp_boss = convert_boolean(comp_boss, ['groove','unique_feature','orientation'])

    base_load(comp_boss, ComponentType, COLUMNS_MAP['component_type'], session)
    base_load(comp_boss, ConnectionType, COLUMNS_MAP['connection_type'], session)
    base_load(comp_boss, Component, COLUMNS_MAP['component'], session)

    bill_of_materials = base_read(PATHS['material_bill'])
    bill_of_materials = normalize(bill_of_materials, 'tube_assembly_id', ['component_id','quantity'], 8)

    base_load(bill_of_materials, MaterialBill, COLUMNS_MAP['material_bill'], session)

if __name__ == "__main__":

    create_db()
    session = Session()
    main()
