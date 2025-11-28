"use strict";
//2 Fetch data from the API from js
async function fetchProducts() {
    const API_URL = 'https://dummyjson.com/products';
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data.products;
    }
    catch (error) {
        console.error('Could not fetch the API url', error);
        return [];
    }
}
//3 Display products
function displayProducts(products) {
    const productList = document.getElementById('product-list');
    if (!productList)
        return;
    productList.innerHTML = '';
    products.forEach(product => {
        const li = document.createElement('li');
        li.textContent = `${product.title} -`;
        const priceStrong = document.createElement('strong');
        priceStrong.textContent = `${product.price}`;
        li.appendChild(priceStrong);
        productList.appendChild(li);
        const productImage = document.createElement('img');
        productImage.src = product.images[0];
        productImage.alt = product.title;
        productImage.height = 100;
        productImage.width = 100;
        li.appendChild(productImage);
    });
}
//4 call functions
async function main() {
    const products = await fetchProducts();
    displayProducts(products);
}
//5 When DOM LOADED call the main function
document.addEventListener('DOMContentLoaded', main);
