from flask import request, flash, render_template , redirect

from auth import check_password , hash_password

from routes import app


@app.get('/log_in/')
def log_get():
    return render_template('log_in.html')

@app.post('/log_in/')
def log_post():
    name = request.form['name']
    password = request.form['password']



