import sqlite3

from connection import do_connect


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

def check_user_by_email(email):
    if email == None:
        return None
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM users WHERE email=?'''


        cursor.execute(sqlite_query_check_table,(email,))
        sql_con.commit()
        data_list = cursor.fetchall()
        if data_list == None:
            return None
        data_list = data_list[0]

        data_dict = {}
        data_dict['id'] = data_list[0]
        data_dict['name'] = data_list[1]
        data_dict['email'] = data_list[2]
        data_dict['password'] = data_list[3]
        data_dict['rule'] = data_list[4]
        data_dict['photo'] = data_list[5]
        return data_dict
    except sqlite3.Error as error:
        print(error)



def check_user_by_name(name):
    if name == None:
        return None
    try:
        sql_con, cursor = do_connect()

        sqlite_query_check_table = '''SELECT * FROM users WHERE name=?'''


        cursor.execute(sqlite_query_check_table,(name,))
        sql_con.commit()
        data_list = cursor.fetchall()
        if data_list == None:
            return None
        data_list = data_list[0]

        data_dict = {}
        data_dict['id'] = data_list[0]
        data_dict['name'] = data_list[1]
        data_dict['email'] = data_list[2]
        data_dict['password'] = data_list[3]
        data_dict['rule'] = data_list[4]
        data_dict['photo'] = data_list[5]
        return data_dict
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

def add_to_table(name,email,password,rule='user',photo='https://i.pinimg.com/736x/59/af/9c/59af9cd100daf9aa154cc753dd58316d.jpg'):
    try:
        sql_con, cursor = do_connect()

        sqlite_query_add_table = '''INSERT INTO users
                                        (name,email,password,rule,photo)
                                        VALUES
                                        (?,?,?,?,?)'''


        cursor.execute(sqlite_query_add_table,(name,email,password,rule,photo,))
        sql_con.commit()
        print('Add in to table')
    except sqlite3.Error as error:
        print(error)

