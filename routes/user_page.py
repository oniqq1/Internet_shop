from flask import render_template
from flask_login import login_required

from flask import render_template

from routes import app

from models.users import check_user_by_name



@app.get('/user/<name>/')
@login_required
def user_page_get(name:str):
    if check_user_by_name(name):
        return "all good"
    else:
        return "You haven't an account"