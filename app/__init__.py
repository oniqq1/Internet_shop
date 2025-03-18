import sqlite3

from flask import Flask, session

from secret import key
from connection import create_table


app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key = key


try:
    create_table()
except sqlite3.Error as error:
    print(error)



