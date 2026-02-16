const quantityInput = document.getElementById('quantity');
const priceSpan = document.getElementById('price');
const totalSpan = document.getElementById('total');
const articleSpan = document.getElementById('article');

function calculateTotal() {
    const quantity = Number(quantityInput.value);
    const price = Number(priceSpan.innerText);

    const total = quantity * price;
    totalSpan.innerText = total

    if (quantity > 1) {
        articleSpan.innerText = 'articles';
    } else {
        articleSpan.innerText = 'article';
    }
}

quantityInput.addEventListener('input', calculateTotal);

calculateTotal();