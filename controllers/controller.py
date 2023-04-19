from app import app
from flask import render_template
from models.orders import orders, get_order


@app.route('/')
def index():
    return render_template('index.jinja', title = 'title', orders = orders)

@app.route('/orders/<id>')
def order(id):
    selected_order = get_order(int(id))
    return render_template('order.html', order=selected_order)