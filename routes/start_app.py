from flask import Flask, render_template

app = Flask(__name__,template_folder='../templates')

@app.get("/test/")
def test():
    return render_template('test.html')