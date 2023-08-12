from flask import session, make_response
from typing import Dict
import json
from app import app

from pprint import pprint


class Cart:
    def __init__(self):
        if session.get("order"):
            self.order = self._load_json(session.get("order"))
        else:
            self.order: Dict[str, (int, dict)] = {
                'order': {},
                'total_cost': 0
            }

    def add_product(self, product: dict):
        orders = self.order['order'].get(product['type'])
        if not orders:
            self.order['order'][product['type']] = [product]
        elif product not in orders:
            orders.append(product)
        else:
            index = [index for index, pr in enumerate(orders) if pr == product][0]
            orders[index]["quantity"] += 1
        self.order["total_cost"] += int(product["cost"])
        self._save_order()

    def decrease_product_quantity(self, product_data: list):
        product_in_order = self._get_product(product_data)
        self.order["total_cost"] -= int(product_in_order['cost'])
        if product_in_order['quantity'] == 1:
            self.order['order'][product_in_order['type']].remove(product_in_order)
        else:
            product_in_order['quantity'] -= 1
        self._save_order()
        print(self.order)

    def increase_product_quantity(self, product_data: list):
        product_in_order = self._get_product(product_data)
        self.order["total_cost"] += int(product_in_order['cost'])
        product_in_order['quantity'] += 1
        self._save_order()

    def get_order(self):
        return self.order

    def _save_order(self):
        session['order'] = self._dump_json(self.order)
        session.modified = True
        app.session_interface.save_session(app, session, make_response("dummy"))

    def _get_product(self, product_data: list):
        product_type = product_data[0]
        product_index = int(product_data[1])
        product_in_order = self.order['order'].get(product_type)[product_index]
        return product_in_order

    @staticmethod
    def _load_json(order):
        return json.loads(order)

    @staticmethod
    def _dump_json(order):
        return json.dumps(order, ensure_ascii=False)


