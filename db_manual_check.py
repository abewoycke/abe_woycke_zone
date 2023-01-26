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

database = "./awz_sqlite.db"
conn = create_connection(database)
c = conn.cursor()

def update_item(c, item):
    sql = ''' UPDATE poll_options
                  SET votes = votes+1
                  WHERE name = ? '''
    c.execute(sql, item)

try:
    update_item(c, ["Saturday 02/25 7pm PT / 10pm ET"])
except Error as e:
    print(e)

def select_all_items(c, name):
    sql = ''' SELECT * FROM poll_options '''
    c.execute(sql)
    rows = conn.fetchall()
    return rows

c.execute('SELECT * FROM poll_options')
output = c.fetchall()
for row in output:
    print(row)

try:
    select_all_items
except Error as e:
    print(e)

try:
    c.execute("UPDATE poll_options SET votes = 0")
except Error as e:
    print(e)