from app import app ,session
from flask import render_template
from app.models.users import check_user_by_name
from app.models.items import get_item_by_id


@app.get('/')
def main():
    if session.get('name') == None:
        return render_template('index.html', img='https://i.pinimg.com/736x/59/af/9c/59af9cd100daf9aa154cc753dd58316d.jpg')
    img = check_user_by_name(session.get('name')).get('photo')
    return render_template('index.html',img=img)


