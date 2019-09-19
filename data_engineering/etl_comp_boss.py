from msc.util import *
from orm.db import *
from orm.model import *
from orm import create_db, Session

def main():

    comp_boss = base_read(PATHS['component_boss'])
    comp_boss = convert_boolean(comp_boss, ['groove','unique_feature','orientation'])

    base_load(comp_boss, ComponentType, COLUMNS_MAP['component_type'], session)
    base_load(comp_boss, ConnectionType, COLUMNS_MAP['connection_type'], session)
    base_load(comp_boss, Component, COLUMNS_MAP['component'], session)

if __name__ == "__main__":

    create_db()
    session = Session()
    main()
