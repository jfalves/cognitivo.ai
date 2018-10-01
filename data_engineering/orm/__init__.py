
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///data/database.db')

Session = sessionmaker(bind=engine)

Base = declarative_base(engine)

from orm.model import *

def create_db():
    Base.metadata.create_all()
