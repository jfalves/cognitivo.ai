import pandas as pd
from sqlalchemy import inspect

def base_read(path):

    df = pd.read_csv(path, parse_dates=True, dayfirst=True)

    return df

def base_lookup(Table,filter,session):

    query = session.query(Table).filter_by(**filter)

    return session.query(query.exists()).scalar()

def base_load(df, Table, column_map, session, commit_size=10000):

    table_map = inspect(Table)

    column_name = [column.name for column in table_map.columns]
    primary_key = [key.name for key in table_map.primary_key]

    df = df.rename(columns=column_map)
    df = df.drop_duplicates(subset=primary_key)
    df = df.set_index(keys=primary_key)

    insert = 0
    total = len(df.index)
    obj_list = []

    for idx, row in df.iterrows():

        # Transforma índice em lista
        if type(idx) != tuple:
            idx = [idx]
        else:
            idx = list(idx)

        filter = dict(zip(primary_key,idx))
        idx.extend(row)
        data = dict(zip(column_name,idx))

        if not base_lookup(Table,filter,session):

            table_instance = Table(**data)
            obj_list.append(table_instance)
            insert += 1

            if (insert % commit_size == 0) or (insert == total):
                session.bulk_save_objects(obj_list)
                session.commit()
                obj_list.clear()

    print('Tabela: {0} (ins:{1})'.format(Table.__tablename__,insert))
