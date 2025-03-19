import sqlite3

from connection import do_connect


def drop_table():
    try:
        sql_con, cursor = do_connect()

        sqlite_query_drop_table = '''DROP TABLE items
                                         '''
        cursor.execute(sqlite_query_drop_table)
        sql_con.commit()
        print('Table dropped items')
    except sqlite3.Error as error:
        print(error)

def get_item_by_id(id):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM items WHERE id=?'''


        cursor.execute(sqlite_query_check_table,(id,))
        sql_con.commit()
        return cursor.fetchone()
    except sqlite3.Error as error:
        print(error)


def get_item_by_name(name):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM items WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        return cursor.fetchone()
    except sqlite3.Error as error:
        print(error)


def add_to_table(name,description,cost,photo='https://i.pinimg.com/736x/70/8c/08/708c08614099f90b849c6f7089f8effb.jpg'):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_add_table = '''INSERT INTO items
                                        (name,description,cost,photo)
                                        VALUES
                                        (?,?,?,?)'''


        cursor.execute(sqlite_query_add_table,(name,description,cost,photo,))
        sql_con.commit()
        print('Add in to table items')
    except sqlite3.Error as error:
        print(error)

