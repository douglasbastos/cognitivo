import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#
# USER = 'root'
# PWD = 'root'
# HOST = 'localhost'
# DB_NAME = 'test_database'
#

# SQLALCHEMY_CONN_STR = f"mysql+pymysql://{USER}:{PWD}@{HOST}/{DB_NAME}"

# engine = create_engine(SQLALCHEMY_CONN_STR)
# session = scoped_session(sessionmaker(bind=engine))
#
#
# metadata = MetaData()

engine = create_engine('sqlite:///../sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
