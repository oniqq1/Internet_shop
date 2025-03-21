from app import app ,session
from flask import render_template
from app.models.users import check_user_by_name



@app.get('/user/<name>/')
def user_page_get(name:str):
    print(session.get('name'))
    print(check_user_by_name(session.get('name')))
    if session.get('name') == check_user_by_name(session.get('name')).get('name'):
        if check_user_by_name(name):
            user = check_user_by_name(name)
            print(user)
            return render_template('home_page.html',user=user)
        else:
            return f'No such account'
    else:
        f'You dont in account'
    return 'hello'