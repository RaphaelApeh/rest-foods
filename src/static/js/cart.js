console.log("What slslsls")
const cartPanel = document.querySelector('#cart-panel');
const cartOverlay = document.querySelector('#overlay');
const cartBody = document.querySelector('#body');
const cartClose = document.querySelector('#close-cart-panel');

// cart
const objectName = document.querySelector("#object-name").textContent.trim();
const objectPrice = document.querySelector("#object-price");
const objectDescription = document.querySelector("#object-description");
const objectImg = document.querySelector("#object-image");

console.log(document.querySelector("#get-data"))

document.querySelectorAll('.cart').forEach(cart => {
    cart.addEventListener('click', event => {
        cartOverlay.classList.remove('hidden');
        cartBody.classList.add('overflow-hidden');
        cartPanel.classList.remove('translate-x-full');
        cartPanel.classList.add('-translate-x-0');
    });
});


cartOverlay.addEventListener('click', event => {
    cartOverlay.classList.add('hidden');
    cartBody.classList.remove('overflow-hidden');
    cartPanel.classList.remove('-translate-x-0');
    cartPanel.classList.add('translate-x-full');
});

cartClose.addEventListener('click', event => {
    cartOverlay.classList.add('hidden');
    cartBody.classList.remove('overflow-hidden');
    cartPanel.classList.remove('-translate-x-0');
    cartPanel.classList.add('translate-x-full');
})

document.querySelector("#get-data").addEventListener("click", function(){
    fetch(`/api/foods/${objectName}/`)
    .then(response => response.json())
    .then(data=> {
        console.log(data)
        objectDescription.textContent = data.short_description;
        objectImg.src = data.image;
        objectPrice.textContent = data.price
    })
    .catch(error=> console.log("Error", error))
})