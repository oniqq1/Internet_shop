import sqlite3
import bcrypt
from app import app
from flask import render_template , request ,session
from ..models.users import check_user_by_name , get_password , add_to_table

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




@app.get('/sign_up/')
def sign_up_get():

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


    session['name'] = name
    session['email'] = email


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