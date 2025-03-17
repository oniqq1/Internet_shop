import sqlite3
import bcrypt
from app import app
from flask import render_template , request
from ..models.users import check_user_by_name , get_password , add_to_table
from ..models import User
from flask_login import login_user
from connection import do_connect


@app.get('/log_in/')
def log_in_get():
    return render_template('log_in.html')

@app.post('/log_in/')
def log_in_post():
    name = request.form['name']
    password = request.form['password']

    if not check_user_by_name(name):
        return 'error'

    if not check_password(get_password(name),password):
        return 'error'

    user_data = check_user_by_name(name)[0]

    user_object = User(id=user_data[0],username=user_data[1],gmail=user_data[2],password=user_data[3],rule=user_data[4],photo=user_data[5])

    login_user(user_object,remember=True)


@app.get('/sign_up/')
def sign_up_get():
    print('hello')
    return render_template('sign_up.html')

@app.post('/sign_up/')
def sign_up_post():
    print('in')
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if not name and password and email:
        return render_template('sign_up.html')
    print('check complete')

    try:
        connection , cursor = do_connect()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        connection.close()
        print(user)

        if user:

            if not email == user[2]:

                return render_template('sign_up.html')




    except sqlite3.Error as error:
        print(error)

    hash = hash_password(password)

    add_to_table(name, email, hash)

    user_in_db = check_user_by_name(name)[0]
    print(user_in_db)
    print(user_in_db[0])

    user_new = User(id=user_in_db[0], name=user_in_db[1],email=user_in_db[2], password=user_in_db[3],
                    rule=user_in_db[4], photo=user_in_db[5])

    login_user(user_new)

    return 'registered'

@app.get('/log_out/')
def log_out():
    pass


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode(),salt=salt)
    return hashed

def check_password(password , hashed):
    return bcrypt.checkpw(password.encode(),hashed)