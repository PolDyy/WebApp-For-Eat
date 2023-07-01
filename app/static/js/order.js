
class Order {

    constructor() {
        let data = JSON.parse(sessionStorage.getItem('order'))
        this.order = data.order
        this.total_cost = data.total_cost
        console.log(data)
    }

    increaseQuantity(key, index) {
        let item = this.order[key][index];
        item.quantity += 1;
        this.total_cost += item.cost;
        this.updateSessionData();
        return item.quantity;
    }

    decreaseQuantity(key, index) {
        let item = this.order[key][index];
        if (item.quantity > 0) {
            item.quantity -= 1;
            this.total_cost -= item.cost;
            this.updateSessionData();
            return item.quantity;}
        return 0;
    }

    updateSessionData() {
    let data = {
        order: this.order,
        total_cost: this.total_cost
        };
    sessionStorage.setItem('order', JSON.stringify(data));
    }
}

let order = new  Order();
const addButton = document.querySelectorAll('.order-product__add');
const removeButton = document.querySelectorAll('.order-product__remove');
const totalPrice = document.getElementById('total-cost');

addButton.forEach((button) => {
    button.addEventListener('click', (event) => {
        let dataProduct = event.target.getAttribute('data-product').split(", ");
        let quantity = order.increaseQuantity(dataProduct[0], Number(dataProduct[1]));
        totalPrice.textContent=order.total_cost + " ₽";
        event.target.previousElementSibling.textContent = quantity;
    });
});
removeButton.forEach((button) => {
    button.addEventListener('click', (event) => {
        let dataProduct = event.target.getAttribute('data-product').split(", ")
        let quantity = order.decreaseQuantity(dataProduct[0], Number(dataProduct[1]))
        totalPrice.textContent=order.total_cost  + " ₽";
        event.target.nextElementSibling.textContent = quantity;
    });
});

window.addEventListener('pagehide', function (event){
   let data = sessionStorage.getItem('order');

   // navigator.sendBeacon('/update-cart', data);
   let xhr = new XMLHttpRequest();
   xhr.open('POST', '/update-cart', false);
   xhr.setRequestHeader('Content-Type', 'application/json');
   xhr.send(data);

});