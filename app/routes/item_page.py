from app import app ,session
from flask import render_template
from app.models.items import get_item_by_id


@app.get('/item/<id>')
def item(id):
    item = get_item_by_id(id)
    return render_template('item.html', item=item)