from app import app ,session
from flask import render_template
from app.models.users import check_user_by_name



@app.get('/main/')
def main():
    return render_template('index.html')