from app import app
from flask import render_template, session
from app.models.users import check_user_by_name



@app.get('/user/<name>/')
def user_page_get(name:str):
    if session.get('name') in check_user_by_name(session.get('name')):
        if check_user_by_name(name):
            return render_template('user_page.html',data=check_user_by_name(name))
        else:
            return render_template('No such account')