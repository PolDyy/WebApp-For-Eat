from flask import session
from typing import Dict
import json


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

    def update_cart(self, order):
        self.order = order
        self._save_order()

    def remove(self, index: int, product_type):
        product_in_order = self.order['order'].get(product_type)[index]
        self.order["total_cost"] -= int(product_in_order['cost'])
        if product_in_order['quantity'] == 1:
            del product_in_order
        else:
            product_in_order['quantity'] -= 1
        self._save_order()

    def get_order(self):
        return self.order

    def _save_order(self):
        session['order'] = self._dump_json(self.order)
        session.modified = True

    @staticmethod
    def _load_json(order):
        return json.loads(order)

    @staticmethod
    def _dump_json(order):
        return json.dumps(order, ensure_ascii=False)

