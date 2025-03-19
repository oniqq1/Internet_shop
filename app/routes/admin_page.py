

from flask import render_template, session

from app import app

from app.models.users import check_user_by_name



@app.get('/user/<name>/')
def admin_page_get(name:str):
    if session.get('name') in check_user_by_name(session.get('name')):
        if check_user_by_name(name).get('rule') == 'admin':
            return render_template('admin_page.html')
        else:
            return render_template('index.html')