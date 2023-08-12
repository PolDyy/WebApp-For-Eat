
class Order {

    constructor(json_order) {
        let data = JSON.parse(json_order)
        this.order = data.order
        this.total_cost = data.total_cost
        console.log(data)
    }

    increaseQuantity(key, index) {
        let item = this.order[key][index];
        item.quantity += 1;
        this.total_cost += item.cost;
        return item.quantity;
    }

    decreaseQuantity(key, index) {
        let item = this.order[key][index];
        if (item.quantity > 0) {
            item.quantity -= 1;
            this.total_cost -= item.cost;
            return item.quantity;
        }
        return 0;
    }
}


let order;
const addButton = document.querySelectorAll('.order-product__add');
const removeButton = document.querySelectorAll('.order-product__remove');
const totalPrice = document.getElementById('total-cost');

document.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port)

    socket.on('connect', () => {
        console.log("Connected")
    });

    socket.on('action_load_order', (order_data) => {
        order = new Order(order_data)
    });

    addButton.forEach((button) => {
        button.addEventListener('click', (event) => {
            let dataProduct = event.target.getAttribute('data-product').split(", ");
            let quantity = order.increaseQuantity(dataProduct[0], Number(dataProduct[1]));
            totalPrice.textContent=order.total_cost + " ₽";
            event.target.previousElementSibling.textContent = quantity;
            socket.emit('action_add_product', JSON.stringify(dataProduct));
        });
    });

    removeButton.forEach((button) => {
        button.addEventListener('click', (event) => {
            let dataProduct = event.target.getAttribute('data-product').split(", ")
            let quantity = order.decreaseQuantity(dataProduct[0], Number(dataProduct[1]))
            totalPrice.textContent=order.total_cost  + " ₽";
            if (quantity <= 0) {
                let productElement = button.closest('.row');
                productElement.parentNode.removeChild(productElement);
            } else {
                event.target.nextElementSibling.textContent = quantity;
            }
            socket.emit('action_remove_product', JSON.stringify(dataProduct));
        });
    });
})
