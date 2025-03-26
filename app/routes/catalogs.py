from app import app ,session
from flask import render_template, redirect, request
from app.models.users import check_user_by_name
from app.models.items import get_item_by_id , get_items
from random import randint



@app.get('/')
def main():
    items = []
    for i in range(3):
        items.append(get_item_by_id(randint(1,len(get_items()))))

    print(items)

    if session.get('name') == None:
        return render_template('index.html', img='https://i.pinimg.com/736x/59/af/9c/59af9cd100daf9aa154cc753dd58316d.jpg', item1=items[0], item2=items[1], item3=items[2])

    img = check_user_by_name(session.get('name')).get('photo')
    return render_template('index.html',img=img, item1=items[0], item2=items[1], item3=items[2])


@app.get('/catalog/')
def catalog_get():
    if session.get('name') == None:
        data=get_items()
        return render_template('catalog.html',data=data)
    return redirect('/')


@app.post('/catalog/')
def catalog_post():
    if session.get('name') == None:
        search = request.form.get('search')
        data=get_items()
        new_data = []
        for item in data:
            if search in item.get('name'):
                new_data.append(item)
        return render_template('catalog.html',data=new_data)
    return redirect('/')