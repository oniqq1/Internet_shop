from flask import request,  render_template

from auth import check_password

from models.users import check_user_by_name , get_password , check_rule

from routes import app

from routes.start_app import login_manager

@app.get('/log_in/')
def log_get():
    return render_template('log_in.html')

@login_manager.user_loader
@app.post('/log_in/')
def log_post():
    name = request.form['name']
    password = request.form['password']

    if name == None:
        return render_template('log_in.html')

    if check_user_by_name(name):
        if check_password(password,get_password(name)[0]):
            if check_rule(name) == 'admin':
                return render_template('admin.html')
            return render_template('user.html')
        else:
            return render_template('log_in.html')
    else:
        return render_template('log_in.html')