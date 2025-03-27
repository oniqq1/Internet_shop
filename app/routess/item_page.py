from app import app ,session
from flask import render_template , redirect
from app.modelss.items import get_item_by_id
from app.modelss.users import add_to_busket , check_user_by_name


@app.get('/item/<id>')
def item_get(id):
    if check_user_by_name(session.get("name")) == None:
        return redirect('/')

    item = get_item_by_id(id)
    return render_template('item.html', item=item)


@app.post('/item/<id>')
def item_post(id):
    if check_user_by_name(session.get("name")) == None:
        return redirect('/')

    item = get_item_by_id(id)

    user = check_user_by_name(session.get("name"))
    busket = user.get('busket').split()
    id_is = False

    for id_item in busket:
        if id_is == True: break
        if id_item == id:
            id_is = True

    if id_is == False:
        add_to_busket(user.get('name'),id)
    else:
        return render_template('item.html', item=item , code=423)
    return render_template('item.html', item=item)

