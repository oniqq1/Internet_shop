import sqlite3

def do_connect():
    sql_con = sqlite3.connect("users.db")
    cursor = sql_con.cursor()

    return sql_con , cursor

def create_table():
    connection = sqlite3.connect("users.db")
    with open("schema.sql") as f:
        connection.executescript(f.read())