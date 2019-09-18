import pandas as pd
from sqlalchemy import inspect
import fnmatch


PATHS = {'price_quote':'data/price_quote.csv'
       ,'material_bill':'data/bill_of_materials.csv'
       ,'component_boss':'data/comp_boss.csv'}

COLUMNS_MAP = {'supplier':{'supplier':'id'}
              ,'tube_assembly':{'tube_assembly_id':'id'}
              ,'component_type':{'component_type_id':'id'}
              ,'connection_type':{'connection_type_id':'id'}
              ,'component':{'component_id':'id'
                            ,'component_type_id':'component_type_id'
                            ,'connection_type_id':'connection_type_id'
                            ,'type':'type'
                            ,'outside_shape':'outside_shape'
                            ,'base_type':'base_type'
                            ,'height_over_tube':'height_over_tube'
                            ,'bolt_pattern_wide':'bolt_pattern_wide'
                            ,'bolt_pattern_long':'bolt_pattern_long'
                            ,'groove':'groove'
                            ,'base_diameter':'base_diameter'
                            ,'shoulder_diameter':'shoulder_diameter'
                            ,'unique_feature':'unique_feature'
                            ,'orientation':'orientation'
                            ,'weight':'weight'}
              ,'material_bill':{'tube_assembly_id':'tube_assembly_id'
                               ,'component_id':'component_id'
                               ,'quantity':'quantity'}
              ,'price_quote':{'tube_assembly_id':'tube_assembly_id'
                             ,'supplier':'supplier_id'
                             ,'quote_date':'quote_date'
                             ,'annual_usage':'annual_usage'
                             ,'min_order_quantity':'min_order_quantity'
                             ,'bracket_pricing':'bracket_pricing'
                             ,'quantity':'quantity'
                             ,'cost':'cost'}}

def normalize(df, index, columns, level):

    df_normal = pd.DataFrame()

    for lvl in range(1, level+1):
        columns_to_normalize = []

        for column in columns:
            column_match = fnmatch.filter(df.columns, column+'*'+str(lvl))
            columns_to_normalize.append(column_match[0])

        columns_new_names = dict(zip(columns_to_normalize, columns))
        df_sliced = df.rename(columns=columns_new_names)

        columns.append(index)
        df_normal = pd.concat([df_normal, df_sliced[columns]])
        columns.remove(index)

    return df_normal.dropna()

def convert_boolean(df, columns):

    for each in columns:
         df[each].replace(('Yes', 'No'), (True, False), inplace = True)

    return df

def convert_datetime(df, columns):

    for each in columns:
        df[each] = pd.to_datetime(df[each])

    return df

def object_as_dict(obj):

    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
