from flask import request, abort, render_template

from routes import app

from models.users import add_to_table ,check_email

from auth import hash_password

from flask import redirect


@app.get('/reg/')
def registration_get():
    return render_template('registration.html')

@app.post('/reg/')
def registration_post():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if email == None:
        return render_template('registration.html')

    if check_email(email) == []:
        add_to_table(name,email, hash_password(password))

        return render_template('log_in.html')
    return render_template('registration.html')