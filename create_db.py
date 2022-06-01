import sqlite3
from sqlite3 import Error

# creates connection to database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file) # if doesn't find file automatically creates one
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"ENTER_PATH")
