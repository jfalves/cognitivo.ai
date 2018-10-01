import pandas as pd
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

def normalize(df, columns, level):

    df_columns = df.columns
    col1 = df_columns[0]

    frames = pd.DataFrame()

    for lvl in range(1, level+1):
        normalized_col = []

        for column in columns:
            match = fnmatch.filter(df_columns, column+'*'+str(lvl))
            normalized_col.append(match[0])

        renamed_col = dict(zip(normalized_col, columns))
        df.rename(columns=renamed_col, inplace=True)

        columns_tmp = columns
        columns_tmp.append(col1)
        frames = pd.concat([frames,df[columns_tmp]])
        columns_tmp.remove(col1)
        df.drop(columns=columns_tmp, inplace=True)

    return  frames

def convert_boolean(df, columns):

    for each in columns:
         df[each].replace(('Yes', 'No'), (True, False), inplace = True)

    return df
