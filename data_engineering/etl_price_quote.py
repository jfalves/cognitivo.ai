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

if __name__ == "__main__":

    create_db()
    session = Session()
    main()
