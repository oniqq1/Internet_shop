from routes import app

from models.users import check_name , get_id

import flask_login

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(name):
    if check_name(name):
        return

    user = User()
    user.id = get_id(name)
    return user


@login_manager.request_loader
def request_loader(request):
    name = request.form.get('name')
    if check_name(name):
        return

    user = User()
    user.id = get_id(name)
    return user