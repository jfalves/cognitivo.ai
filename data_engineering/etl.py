from msc.util import *
from orm.db import *
from orm.model import *
from orm import create_db, Session

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
