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
                                         name TEXT UNIQUE NOT NULL ,
                                         email TEXT NOT NULL UNIQUE,
                                         password TEXT NOT NULL,
                                         rule TEXT NOT NULL)
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

def check_email(email):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM users WHERE email=?'''


        cursor.execute(sqlite_query_check_table,(email,))
        sql_con.commit()
        return cursor.fetchall()
    except sqlite3.Error as error:
        print(error)

def check_name(name):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM users WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        return cursor.fetchall()
    except sqlite3.Error as error:
        print(error)

def check_rule(name):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT rule FROM users WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        return cursor.fetchone()
    except sqlite3.Error as error:
        print(error)

def get_password(name):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT password FROM users WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        return cursor.fetchone()
    except sqlite3.Error as error:
        print(error)

def get_id(name):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT id FROM users WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        return cursor.fetchone()
    except sqlite3.Error as error:
        print(error)

def add_to_table(name,email,password,rule='user'):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_add_table = '''INSERT INTO users
                                        (name,email,password,rule)
                                        VALUES
                                        (?,?,?,?)'''


        cursor.execute(sqlite_query_add_table,(name,email,password,rule,))
        sql_con.commit()
        print('Add in to table')
    except sqlite3.Error as error:
        print(error)

