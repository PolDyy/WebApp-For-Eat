

class Order {
    constructor() {
        let data = JSON.parse(sessionStorage.getItem('order'))
        this.order = data.order
        this.total_price = data.total_price
    }
}