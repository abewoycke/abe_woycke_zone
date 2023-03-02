import os
import sqlite3
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database=database,
                               isolation_level=None,
                               check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(e)

def create_tables(c):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sql_path = os.path.join(BASE_DIR, 'create_polling_db.sql')
    with open(sql_path,'r') as sql_file:
        sql = sql_file.read()
    c.executescript(sql)

def db_setup():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(BASE_DIR, "./awz_sqlite.db")
    conn = create_connection(database)
    c = conn.cursor()
    create_tables(c)

def init_conn():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(BASE_DIR, "./awz_sqlite.db")
    conn = create_connection(database)
    global c
    c = conn.cursor()
    return c

if __name__ == '__main__':
    db_setup()