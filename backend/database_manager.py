```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # create a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def save_code_snippet(conn, code_snippet):
    sql = ''' INSERT INTO code_snippets(language,code)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, code_snippet)
    return cur.lastrowid

def get_code_snippet(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM code_snippets WHERE id=?", (id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_code_snippets_table = """ CREATE TABLE IF NOT EXISTS code_snippets (
                                        id integer PRIMARY KEY,
                                        language text NOT NULL,
                                        code text NOT NULL
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_code_snippets_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```