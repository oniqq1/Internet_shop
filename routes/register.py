from flask import request, flash, render_template

from start_app import app

from models.users import add_to_table

from auth import hash_password

from flask import redirect


@app.get('/registration/')
def registration_get():
    return render_template('registration.html')

@app.post('/registration/')
def registration_post():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if not name or not email or not password:
        flash("Name or email or password are not exist")

    add_to_table(name,email, hash_password(password))

    redirect("log_in.html")