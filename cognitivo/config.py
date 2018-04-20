import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

USE_MYSQL = os.environ.get('USE_MYSQL', '0') == '1'
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PWD = os.environ.get('MYSQL_PWD', '')
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME', 'my_database')

SQLALCHEMY_CONN_STR = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB_NAME}"


if USE_MYSQL:
    engine = create_engine(SQLALCHEMY_CONN_STR)
else:
    engine = create_engine('sqlite:///../cognitivo.db')

DBSession = sessionmaker(bind=engine)
