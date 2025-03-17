from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, email, password, rule , photo):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.rule = rule
        self.photo = photo

    def get_id(self):
        return str(self.id)
