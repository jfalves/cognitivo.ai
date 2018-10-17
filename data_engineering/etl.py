from msc.util import normalize, convert_boolean,  object_as_dict, COLUMNS_MAP, PATHS
from orm import create_db, engine, Session
from orm.model import *
import pandas as pd
from sqlalchemy import inspect
from sqlalchemy.sql.expression import and_

def base_read(path):
    df = pd.read_csv(path, parse_dates=True, dayfirst=True)

    return df

def base_load(df, table, column_map, engine):
    table_map = inspect(table)

    column_name = [column.name for column in table_map.columns]
    primary_key = [key.name for key in table_map.primary_key]

    df = df.rename(columns=column_map)
    df = df[column_name]
    df = df.drop_duplicates(subset=primary_key)
    df = df.set_index(keys=primary_key)

    df.to_sql(table.__tablename__, con=engine, if_exists='append', index_label=primary_key)

def main():
    price_quote = base_read(PATHS['price_quote'])
    price_quote = convert_boolean(price_quote,['bracket_pricing'])

    base_load(price_quote, Supplier, COLUMNS_MAP['supplier'], engine)
    base_load(price_quote, TubeAssembly, COLUMNS_MAP['tube_assembly'], engine)
    base_load(price_quote, PriceQuote,COLUMNS_MAP['price_quote'], engine)

    comp_boss = base_read(PATHS['component_boss'])
    comp_boss = convert_boolean(comp_boss, ['groove','unique_feature','orientation'])

    base_load(comp_boss, ComponentType, COLUMNS_MAP['component_type'], engine)
    base_load(comp_boss, ConnectionType, COLUMNS_MAP['connection_type'], engine)
    base_load(comp_boss, Component, COLUMNS_MAP['component'], engine)

    bill_of_materials = base_read(PATHS['material_bill'])
    bill_of_materials = normalize(bill_of_materials, ['component_id','quantity'], 8)
    bill_of_materials = bill_of_materials.dropna(subset=['component_id'])

    base_load(bill_of_materials, MaterialBill, COLUMNS_MAP['material_bill'], engine)

if __name__ == "__main__":
    create_db()
    session = Session()
    main()
