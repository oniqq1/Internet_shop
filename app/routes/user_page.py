from flask_login import login_required

from app import app

from app.models.users import check_user_by_name



@app.get('/user/<name>/')
@login_required
def user_page_get(name:str):
    if check_user_by_name(name):
        return "all good"
    else:
        return "No such account"