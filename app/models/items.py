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
        data_item = cursor.fetchall()
        if data_item == None:
            return None
        data_item = data_item[0]

        data_dict = {}
        data_dict['id'] = data_item[0]
        data_dict['name'] = data_item[1]
        data_dict['description'] = data_item[2]
        data_dict['category'] = data_item[3]
        data_dict['cost'] = data_item[4]
        data_dict['photo'] = data_item[5]
        return data_dict
    except sqlite3.Error as error:
        print(error)

def get_items():
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM items'''


        cursor.execute(sqlite_query_check_table)
        sql_con.commit()
        data_item = cursor.fetchall()
        if data_item == None:
            return None
        fetch_data = [0]


        for item in data_item:
            data_dict = {}
            data_dict['id'] = item[0]
            data_dict['name'] = item[1]
            data_dict['description'] = item[2]
            data_dict['category'] = item[3]
            data_dict['cost'] = item[4]
            data_dict['photo'] = item[5]
            fetch_data.append(data_dict)




        return fetch_data
    except sqlite3.Error as error:
        print(error)


def get_item_by_name(name):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM items WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        data_item = cursor.fetchall()
        if data_item == None:
            return None
        data_item = data_item[0]

        data_dict = {}
        data_dict['id'] = data_item[0]
        data_dict['name'] = data_item[1]
        data_dict['description'] = data_item[2]
        data_dict['category'] = data_item[3]
        data_dict['cost'] = data_item[4]
        data_dict['photo'] = data_item[5]
        return data_dict
    except sqlite3.Error as error:
        print(error)


def add_to_table(name,description,cost,category='something',photo='https://i.pinimg.com/736x/70/8c/08/708c08614099f90b849c6f7089f8effb.jpg'):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_add_table = '''INSERT INTO items
                                        (name,description,cost,category,photo)
                                        VALUES
                                        (?,?,?,?,?)'''


        cursor.execute(sqlite_query_add_table,(name,description,cost , category,photo,))
        sql_con.commit()
        print('Add in to table items')
    except sqlite3.Error as error:
        print(error)

