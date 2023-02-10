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
            CREATE TABLE IF NOT EXISTS dim_participant (
                participant_pk INTEGER PRIMARY KEY,
                submitted_name TEXT NOT NULL
            )
            CREATE TABLE IF NOT EXISTS dim_poll (
                poll_pk INTEGER PRIMARY KEY,
                month INTEGER NOT NULL,
                year INTEGER NOT NULL,
                squad TEXT NOT NULL
            )
            CREATE TABLE IF NOT EXISTS fact_response (
                response_pk INTEGER PRIMARY KEY,
                participant_fk INTEGER NOT NULL,
                poll_fk INTEGER NOT NULL,
                submitted_dt INTEGER NOT NULL,
                poll_option TEXT NOT NULL,
                response INTEGER DEFAULT 0,
                FOREIGN KEY (participant_fk)
                    REFERENCES dim_participant (participant_pk)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION
                FOREIGN KEY (poll_fk)
                    REFERENCES dim_poll (poll_pk)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION
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