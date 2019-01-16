from flask import render_template

from app import app


@app.route('/')
def hello():
    user = {'username': 'Miguel'}
    shop_items = ['fish','chops', 'meat', 'soup']
    return render_template('index.html', title='Home', user=user, shop_items=shop_items)

@app.route('/irp')
def ireporter_home():
    pass



