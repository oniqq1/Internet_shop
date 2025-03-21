from app import app ,session
from flask import render_template ,redirect
from app.models.users import check_user_by_name



@app.get('/user/<name>/')
def user_page_get(name:str):
    print(name , 'name')
    print(session.get("name"))
    if check_user_by_name(session.get("name")) == None:
        return redirect('/register/')
    user = check_user_by_name(name)
    if not user == None:
        if session.get('name') == check_user_by_name(name).get('name'):
            return render_template('home_page.html',user=user)
        else:
            return f'No such account'
    else:
        return "It isn't your account  <a href='/main/'>Go back</a>"
    return 'hello'