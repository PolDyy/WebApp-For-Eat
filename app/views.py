from flask import render_template, request, jsonify
import json

from . import app
from . import socketio
from .services.product import Product, Additive
from .services.context import get_popup_header
from .services.form_processing import add_product_form_processing
from .services.cart import Cart
from .forms import ProductForm


@app.route("/")
def index():
    return render_template("main.html")


@app.route('/get_order', methods=['GET'])
def get_order():
    order = Cart().get_order()
    return render_template('order.html', order=order)


@app.route("/product/add", methods=["POST"])
def add_product():
    form = ProductForm(request.form)
    result = add_product_form_processing(form)
    return jsonify(result)

# @app.route('/update-cart', methods=['POST'])
# def update_cart():
#     order = json.loads(request.get_data())
#     Cart().update_cart(order)
#     return "ok"


@socketio.on('action_remove_product', methods=['POST'])
def action_remove_product(pr_type, pr_id):
    order = json.loads(request.get_data())
    Cart().update_cart(order)
    return "ok"


@socketio.on('action_add_product', methods=['POST'])
def action_add_product(pr_type, pr_id):
    order = json.loads(request.get_data())
    Cart().update_cart(order)
    return "ok"


@app.context_processor
def context_processor():
    return dict(products=Product(),
                additive=Additive().get_additive(),
                exceptions=Additive().get_exceptions(),
                get_popup_header=get_popup_header,
                product_form=ProductForm(),
                )


