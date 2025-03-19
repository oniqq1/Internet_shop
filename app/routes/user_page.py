from app import app ,session

from app.models.users import check_user_by_name



@app.get('/user/<name>/')
def user_page_get(name:str):
    if session.get('name') in check_user_by_name(session.get('name')):
        if check_user_by_name(name):
            return "all good"
        else:
            return "No such account"