const pizzaSelect = document.getElementById("pizza");

const withSupRadio = document.getElementById("withSup");
const noSupRadio = document.getElementById("noSup");
const supZone = document.getElementById("supZone");

const supCheckboxes = document.querySelectorAll(".sup");
const priceSpan = document.getElementById("price");

function updatePriceAndUI() {
    // prix des pizzas (tableau associatif)

    const pizzaPrices = {
        margarita: 8,
        regina: 10,
        capricciosa: 11,
        quattro: 10.5,
        diavola: 9.5,
        marinara: 12.5
    };

    const selectedPizza = pizzaSelect.value;
    let total = pizzaPrices[selectedPizza];

    // afficher / cacher les suppléments 

    const withSup = withSupRadio.checked;

    if (withSup) {
        supZone.classList.remove("hidden");
    } else {
        supZone.classList.add("hidden");

        // si "sans supplément", on décoche tout (pour éviter de payer pour rien)
        supCheckboxes.forEach(checkbox => checkbox.checked = false);
    }

    // ajouter le prix des suppléments 
    
    if (withSup) {
        let countSup = 0;
        supCheckboxes.forEach(checkbox => {
            if (checkbox.checked) countSup++;
        });
        total += countSup * 0.5;
    }

    // paiement : +2 euros si visa

    const payment = document.querySelector("input[name='pay']:checked").value;
    if (payment === "visa") {
        total += 2;
    }

    // affichage du prix total
    priceSpan.innerText = total.toFixed(2);
}

// events

pizzaSelect.addEventListener("change", updatePriceAndUI);
withSupRadio.addEventListener("change", updatePriceAndUI);
noSupRadio.addEventListener("change", updatePriceAndUI);

supCheckboxes.forEach(checkbox => checkbox.addEventListener("change", updatePriceAndUI));

document.querySelectorAll("input[name='pay']").forEach(radio => radio.addEventListener("change", updatePriceAndUI));

// init au changement

updatePriceAndUI();