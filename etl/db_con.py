import os
import pyodbc
from sqlalchemy import create_engine


def get_sql_conn():
    """return db connection."""
    #get password from environmnet var
    pwd = os.environ['DAGSTER_POSTGRES_PASSWORD']
    uid = os.environ['DAGSTER_POSTGRES_USER']
    #
    conn = pyodbc.connect(
              'DRIVER=' + 'ODBC Driver 17 for SQL Server' +
              ';server=' + os.environ['DAGSTER_POSTGRES_HOST'] +
              ';database=' + os.environ['DAGSTER_POSTGRES_DB'] +
              ';UID=' + uid +
              ';PWD=' + pwd
              )
    try:
        return conn
    except:
        print("Error loading the config file.")


def get_postgres_creds():
    #get password from environmnet var
    pwd = os.environ['DAGSTER_POSTGRES_PASSWORD']
    uid = os.environ['DAGSTER_POSTGRES_USER']
    #
    server = os.environ['DAGSTER_POSTGRES_HOST']
    db = os.environ['DAGSTER_POSTGRES_DB']
    uid = uid
    pwd = pwd
    port = 5432
    cs = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
    try:
        return cs
    except:
        print("Error loading the config file.")