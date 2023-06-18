class Product:

    products = {
        "Шаурма": [
            {'name': "Курица",
             'cost': ['180', '200', '220'],
             'composition': "Мясо курицы, капуста, помидоры, огурцы, лук, "
                            "морковь по-корейски, картофель фри, соусы, паприка",
             "img_src": "../static/img/kebab64.png"},
            {'name': "Говядина",
             'cost': ["200", '220', '240'],
             'composition': "Говядина, капуста, помидоры, огурцы, лук, "
                            "морковь по-корейски, картофель фри, соусы, паприка",
             "img_src": "../static/img/kebab64.png"},
            {'name': "Mix",
             'cost': ['190', '210', '230'],
             'composition': "Мясо курица/говядина, капуста, помидоры, огурцы, лук, "
                            "морковь по-корейски, картофель фри, соусы, паприка",
             "img_src": "../static/img/kebab64.png"},
        ],
        "Донер": [
            {'name': "Курица",
             'cost': ['180', '200', '220'],
             'composition': "Мясо курицы ,капуста, помидоры, огурцы, лук, "
                            "морковь по-корейски, картофель фри, соусы, паприка",
             "img_src": "../static/img/kebab64.png"},
            {'name': "Говядина",
             'cost': ['200', '220', '240'],
             'composition': "Говядина, капуста, помидоры, огурцы, лук, "
                            "морковь по-корейски, картофель фри, соусы, паприка",
             "img_src": "../static/img/kebab64.png"},
            {'name': "Mix",
             'cost': ['190', '210', '230'],
             'composition': "Мясо курица/говядина, капуста, помидоры, огурцы, "
                            "лук, морковь по-корейски, картофель фри, соусы, паприка",
             "img_src": "../static/img/kebab64.png"},
        ]
    }

    @classmethod
    def get_products(cls):
        return cls.products

    @classmethod
    def get_product(cls, name):
        return cls.products[name]

    @classmethod
    def get_products_names(cls):
        return cls.products.keys()

    @classmethod
    def get_product_cost(cls, product):
        return ", ".join(product['cost'])


class Additive:

    additive = {
            "Картофель фри": 30,
            "Мясо": 40,
            "Капуста": 15,
            "Морковь": 15,
        }
    exceptions = ["Лук", "Перец"]
    
    @classmethod
    def get_additive(cls):
        return cls.additive

    @classmethod
    def get_exceptions(cls):
        return cls.exceptions
