from app import app ,session
from flask import render_template ,redirect ,request
from app.models.users import check_user_by_name ,clear_busket
from app.models.items import add_to_table , get_item_by_id


@app.get('/user/<name>/')
def user_page_get(name:str):

    print(name , 'name')
    print(session.get("name"))


    if check_user_by_name(session.get("name")) == None:
        return redirect('/register/')

    user = check_user_by_name(name)

    if not user == None:

        if session.get('name') == user.get('name'):
            items_id = user.get('busket').split()
            items = []
            for id in items_id:
                items.append(get_item_by_id(id))

            if user.get('rule') == 'admin':
                return render_template('admin.html', items=items)
            return render_template('home_page.html',user=user , items=items)

        else:
            return f"It isn't your account  <a href='/'>Go back</a> "

    else:
        return "no such account <a href='/'>Go back</a>"


@app.post('/user/<name>/')
def user_page_post(name:str):

    print(name , 'name')
    print(session.get("name"))


    if check_user_by_name(session.get("name")) == None:
        return redirect('/register/')

    user = check_user_by_name(name)

    if not user == None:

        if session.get('name') == user.get('name'):
            items_id = user.get('busket').split()
            items = []
            for id in items_id:
                items.append(get_item_by_id(id))
            clear_busket(name)
            return render_template('buyed.html', items=items)

        else:
            return f"It isn't your account  <a href='/'>Go back</a> "

    else:
        return "no such account <a href='/'>Go back</a>"

@app.post('/add_product/')
def add_product_post():
    print(session.get("name")  , ' add product name')


    if check_user_by_name(session.get("name")) == None:
        return redirect('/')

    user = check_user_by_name(session.get("name"))

    if not user == None:

        if user.get('rule') == 'admin':
            name = request.form['name']
            description = request.form['description']
            cost = request.form['cost']
            category = request.form['category']
            photo = request.form['photo']

            add_to_table(name=name,description=description,cost=cost,category=category,photo=photo)
            return "Has been added <a href='/'>Go back</a>"

        return "You aren't administrator <a href='/'>Go back</a>"
