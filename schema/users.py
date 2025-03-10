import sqlite3

def do_connect():
    sql_con = sqlite3.connect("users.db")
    cursor = sql_con.cursor()

    return sql_con , cursor

def create_table():
    try:
        sql_con, cursor = do_connect()

        sqlite_query_create_table = '''CREATE TABLE users
                                        ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                         name TEXT ,
                                         email TEXT NOT NULL UNIQUE,
                                         password TEXT NOT NULL)
                                         '''
        cursor.execute(sqlite_query_create_table)
        sql_con.commit()
        print('Table created')
    except sqlite3.Error as error:
        print(error)

def drop_table():
    try:
        sql_con, cursor = do_connect()

        sqlite_query_drop_table = '''DROP TABLE users
                                         '''
        cursor.execute(sqlite_query_drop_table)
        sql_con.commit()
        print('Table dropped')
    except sqlite3.Error as error:
        print(error)

def add_to_table(name,email,password):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_add_table = '''INSERT INTO users
                                        (name,email,password)
                                        VALUES
                                        (?,?,?)'''


        cursor.execute(sqlite_query_add_table,(name,email,password,))
        sql_con.commit()
        print('Add in to table')
    except sqlite3.Error as error:
        print(error)

create_table()
