import sqlite3
import bcrypt
from app import app , session
from flask import render_template , request  ,redirect
from ..models.users import check_user_by_name , add_to_table

from connection import do_connect


@app.get('/log_in/')
def log_in_get():
    return render_template('log_in.html')

@app.post('/log_in/')
def log_in_post():
    name = request.form['name']
    password = request.form['password']


    user_data = check_user_by_name(name)
    print(user_data , '     user_Data')
    if user_data == None:
        return redirect('/')


    print(check_password(password, user_data.get('password')))

    if check_password(password, user_data.get('password')):
        print(name)
        print(user_data.get('name'))
        print(session.get('name'))
        session['name'] = user_data.get('name')
        session['email'] = user_data.get('email')
        session['password'] = user_data.get('password')
        print(session.get('name'))
        return redirect('/')



@app.get('/register/')
def register():
    session.clear()
    return render_template('registration.html')




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
        user = cursor.fetchall()
        connection.close()
        print(user)
        if not email in user:
            hash = hash_password(password)

            add_to_table(name, email, hash)

            session['name'] = name
            session['email'] = email
            session['password'] = hash
            return redirect('/')
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
    return redirect('/')


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode(),salt=salt)
    return hashed

def check_password(password , hashed):
    return bcrypt.checkpw(password.encode(), hashed)

