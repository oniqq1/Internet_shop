import sqlite3

from flask import Flask
from secret import key
from connection import create_table
from flask_login import LoginManager

app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key = key

login_manager = LoginManager()
login_manager.init_app(app)

try:
    create_table()
except sqlite3.Error as error:
    print(error)



