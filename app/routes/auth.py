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

    user_data = check_user_by_name(name)[0]
    print(user_data[1] , user_data[3])

    if name in user_data:
        print(password)
        print(get_password(name))
        if check_password(password,user_data[3]):
            session['name'] = name
            session['email'] = user_data[2]

            return render_template('index.html')



@app.get('/register/')
def register():
    return render_template('register.html')




@app.get('/sign_up/')
def sign_up_get():
    return render_template('sign_up.html')

@app.post('/sign_up/')
def sign_up_post():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if not name or not password or not email:
        return render_template('sign_up.html')



    try:
        connection , cursor = do_connect()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        connection.close()
        print(user)
        if not email in user:
            hash = hash_password(password)

            add_to_table(name, email, hash)

            session['name'] = name
            session['email'] = email

            return render_template('index.html')
        else:
            return render_template('sign_up.html')
    except sqlite3.Error as error:
        print(error)

@app.get('/test/')
def test():
    print(session.get('name'))
    if session.get('name') in check_user_by_name(session.get('name')):
        return "good"
    return "bad"

@app.get('/log_out/')
def log_out_get():
    return render_template('log_out.html')

@app.post('/log_out/')
def log_out_post():
    session.clear()
    return render_template('index.html')


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode(),salt=salt)
    return hashed

def check_password(password , hashed):
    return bcrypt.checkpw(password.encode(), hashed)

