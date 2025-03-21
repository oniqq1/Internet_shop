from app import app ,session
from flask import render_template ,redirect ,request
from app.models.users import check_user_by_name
from app.models.items import add_to_table


@app.get('/user/<name>/')
def user_page_get(name:str):

    print(name , 'name')
    print(session.get("name"))


    if check_user_by_name(session.get("name")) == None:
        return redirect('/register/')

    user = check_user_by_name(name)

    if not user == None:

        if session.get('name') == user.get('name'):
            if user.get('rule') == 'admin':
                return render_template('admin.html')
            return render_template('home_page.html',user=user)

        else:
            return f"It isn't your account  <a href='/'>Go back</a>"

    else:
        return "no such account"


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
            # cost = request.form['cost']
            # category = request.form['category']
            photo = request.form['photo']

            add_to_table(name,description,cost=100,category=11,photo=photo)
            return 'Has been added'

        return "You aren't administrator"
    return 'helllo'