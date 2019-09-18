
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


connection_string = 'sqlite:///data/database.db'

engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)

Base = declarative_base(engine)

from orm.model import *

def create_db():
    Base.metadata.create_all()
