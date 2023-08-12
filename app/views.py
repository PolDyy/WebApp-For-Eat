from flask import render_template, request, jsonify, session, make_response
from flask_socketio import emit
import json

from app import app
from app import socketio

from .services.product import Product, Additive
from .services.context import get_popup_header
from .services.form_processing import add_product_form_processing
from .services.cart import Cart
from .forms import ProductForm

# Вебсокет не обновляет данные сессии

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/product/add", methods=["POST"])
def add_product():
    form = ProductForm(request.form)
    result = add_product_form_processing(form)
    return jsonify(result)


@app.route('/get_order', methods=['GET'])
def get_order():
    order = Cart().get_order()
    return render_template('order.html', order=order)


@socketio.on('connect')
def connect():
    order = Cart().get_order()
    emit('action_load_order', json.dumps(order))


@socketio.on('action_remove_product')
def action_remove_product(product_data):
    product_data = json.loads(product_data)
    Cart().decrease_product_quantity(product_data)


@socketio.on('action_add_product')
def action_add_product(product_data):
    product_data = json.loads(product_data)
    Cart().increase_product_quantity(product_data)


@app.context_processor
def context_processor():
    return dict(products=Product(),
                additive=Additive().get_additive(),
                exceptions=Additive().get_exceptions(),
                get_popup_header=get_popup_header,
                product_form=ProductForm(),
                )


