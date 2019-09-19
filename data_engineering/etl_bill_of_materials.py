from msc.util import *
from orm.db import *
from orm.model import *
from orm import create_db, Session

def main():

    bill_of_materials = base_read(PATHS['material_bill'])
    bill_of_materials = normalize(bill_of_materials, 'tube_assembly_id', ['component_id','quantity'], 8)

    base_load(bill_of_materials, MaterialBill, COLUMNS_MAP['material_bill'], session)

if __name__ == "__main__":

    create_db()
    session = Session()
    main()
