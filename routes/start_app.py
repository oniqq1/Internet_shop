from flask import Flask, render_template
from secret import key

app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key = key


@app.get("/")
def test():
    return render_template('index.html')