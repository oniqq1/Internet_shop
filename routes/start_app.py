from flask import Flask, render_template
from secret import key

from flask_login import LoginManager
login_manager = LoginManager()

app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key = key
login_manager.init_app(app)


@app.get("/")
def test():
    return render_template('index.html')