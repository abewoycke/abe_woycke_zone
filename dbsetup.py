import sqlite3
from sqlite3 import Error
from dates import sandwich_dates_to_poll

def create_connection(database):
    try:
        conn = sqlite3.connect(database=database,
                               isolation_level=None,
                               check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(e)

def create_table(c):
    sql = """
            CREATE TABLE IF NOT EXISTS poll_options (
                name varchar(225) PRIMARY KEY,
                votes integer Default 0
            );
        """
    c.execute(sql)

def create_item(c, item):
    sql = ''' INSERT INTO poll_options(name)
                  VALUES (?)  '''
    try:
        c.execute(sql, item)
    except:
        print("Error creating item occurred")

def update_item(c, item):
    sql = ''' UPDATE poll_options
                  SET votes = votes+1
                  WHERE name = ? '''
    c.execute(sql, item)

def select_all_items(c, name):
    sql = ''' SELECT * FROM poll_options '''
    c.execute(sql)
    rows = conn.fetchall()
    return rows

def db_setup():
    database = "./awz_sqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    create_table(c)
    for date in sandwich_dates_to_poll():
        create_item(c, [date])

if __name__ == '__main__':
    db_setup()