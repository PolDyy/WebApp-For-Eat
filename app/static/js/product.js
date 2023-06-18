class Product {
    constructor(type, name) {
      this.type = type;
      this.name = name;
      this.size_price = 0;
      this.additives_price = 0;
    }
  
    increasePrice(price) {
      this.additives_price += price;
    }
  
    decreasePrice(price) {
        this.additives_price -= price;
    }
  
    getPrice() {
      return this.size_price + this.additives_price;
    }
  }


let product;
const cardButtons = document.querySelectorAll('.card-button');
const addCheckBoxes = document.querySelectorAll('.addones-checkbox');
const removeCheckBoxes = document.querySelectorAll('.removes-checkbox');
const addButton = document.querySelector(".add-button")
const closePopupBtn = document.getElementById('close-popup');
const sizeButtons = document.querySelectorAll('.popup-size');
const popup = document.getElementById('popup');


// setBotStyle();
clearPopup();

closePopupBtn.addEventListener('click', () => {
    popup.style.display = 'none';
    clearPopup();
    
  });

popup.addEventListener('click', (event) => {
    if (event.target === popup) {
      popup.style.display = 'none';
      clearPopup();
    }
  });

function clearPopup() {
    delete window.product;

    let prices = document.querySelectorAll('.addones-price.green');
    let form = document.getElementById("popup-form");

    form.reset();

    prices.forEach((price) => {
    price.classList.remove('green');
    });
    let checkboxes = [...addCheckBoxes, ...removeCheckBoxes];
    checkboxes.forEach((checkbox) => {
    checkbox.checked = false;
    });
        sizeButtons.forEach((btn) => {
        btn.classList.remove('popup-size__selected')
    });
}

sizeButtons.forEach(function (button) {
    button.addEventListener('click', function(event){
        let cost = event.target.getAttribute('data-cost');
        window.product.size_price = Number(cost);
        document.getElementById('popup-cost').textContent=window.product.getPrice() + "₽";
        document.getElementById('pr_size').value = event.target.textContent;
        document.getElementById('pr_cost').value = window.product.getPrice();
        selectSizeBtn(event.target)
    });
});

function selectSizeBtn(button) {
    sizeButtons.forEach((btn) => {
        btn.classList.remove('popup-size__selected')
    });
    button.classList.add('popup-size__selected')
}

cardButtons.forEach(function(button) {
  button.addEventListener('click', function(event) {
    let product_to_add = event.target.getAttribute("data-product");
    let pr_cost = event.target.getAttribute("data-cost").split(', ');
    window.product = new Product(product_to_add.split(", ")[0], product_to_add.split(", ")[1]);
    document.getElementById('pr_type').value=window.product.type;
    document.getElementById('pr_name').value=window.product.name;
    showPopup(product_to_add, pr_cost);
    
  });
});

function showPopup(product, cost) {
    document.getElementById('popup-h3').textContent = product;
    document.getElementById('popup-size-s').setAttribute("data-cost",  cost[0]);
    document.getElementById('popup-size-m').setAttribute("data-cost",  cost[1]);
    document.getElementById('popup-size-l').setAttribute("data-cost",  cost[2]);
    popup.style.display = 'flex';

}

addCheckBoxes.forEach(function(checkbox){
    checkbox.addEventListener('click', function() {
    let cost = this.closest('.addones-item').querySelector('.addones-price');
    if (this.checked) {
        cost.classList.add('green');
        window.product.increasePrice(Number(cost.textContent.slice(1, -1)));
    } else {
        cost.classList.remove('green');
        window.product.decreasePrice(Number(cost.textContent.slice(1, -1)));
      }
    document.getElementById('popup-cost').textContent=window.product.getPrice() + "₽";
    document.getElementById('pr_cost').value = window.product.getPrice();

    });
});

addButton.addEventListener('click', (e) => {
    const productFrom = new FormData(document.getElementById('popup-form'));
    addProduct(productFrom);
    if (!window.bot.MainButton.isVisible) {
        window.bot.MainButton.show();
    }
    popup.style.display = 'none';
    clearPopup();
})

function addProduct(form, cb){
    fetch("/product/add",{
        method: "POST",
        body: form
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        if (data.status === 'success'){
            console.log(data.message);
        } else {
            console.error(data.message)
        }
    })
    .catch(function(error) {
        console.error("Ошибка:", error);
    })
}

// function setBotStyle() {
//     window.bot.expand();
//     window.bot.MainButton.textColor = '#FFFFFF';
//     window.bot.MainButton.color = '#2cab37';
//     window.bot.MainButton.setText("Смотреть заказ");
// }
