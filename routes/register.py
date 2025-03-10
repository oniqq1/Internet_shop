from flask import request , flash


from start_app import app

@app.get('/registration/')
def registration():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if not name or not email or not password:
        flash("Name or email or password are not exist")

