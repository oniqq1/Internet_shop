from flask import render_template
from flask_login import login_required

from flask import render_template

from routes import app

from models.users import check_user_by_name , check_rule



@app.get('/user/<name>/')
@login_required
def admin_page_get(name:str):
    if check_user_by_name(name):
        if check_rule(name) == 'admin':
            return render_template('admin_page.html')
        else:
            return 'You are not admin'
    else:
        return "You haven't an account"