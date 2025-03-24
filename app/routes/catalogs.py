from app import app ,session
from flask import render_template , redirect
from app.models.users import check_user_by_name
from app.models.items import get_item_by_id , get_count
import random


@app.get('/')
def main():
    nums = []
    items = []
    i = 0
    while len(items) != 3 :

        rand = random.randint(1, get_count())

        if not rand in nums:
            items.append(get_item_by_id(rand))
            nums.append(rand)
    print('######')
    print(nums)
    print('######')
    print(items)

    if session.get('name') == None:
        return render_template('index.html', img='https://i.pinimg.com/736x/59/af/9c/59af9cd100daf9aa154cc753dd58316d.jpg', item1=items[0], item2=items[1], item3=items[2])

    img = check_user_by_name(session.get('name')).get('photo')
    return render_template('index.html',img=img,item1=items[0],item2=items[1],item3=items[2])


@app.get('/catalog/')
def catalog():
    if check_user_by_name(session.get("name")) == None:
        return redirect('/')
    return render_template('catalog.html')