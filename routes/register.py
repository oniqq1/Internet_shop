from flask import request, render_template , redirect

from routes import app

from models.users import add_to_table ,check_email

from auth import hash_password




@app.get('/reg/')
def registration_get():
    return render_template('sign_up.html')

@app.post('/reg/')
def registration_post():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if email == None:
        return render_template('sign_up.html')

    if check_email(email) == []:
        add_to_table(name,email, hash_password(password))

        return redirect('log_in.html')
    return render_template('sign_up.html')