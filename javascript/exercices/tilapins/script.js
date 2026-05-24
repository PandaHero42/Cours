document.addEventListener("DOMContentLoaded", function() {
let boutons = document.querySelectorAll(".bouton");
let total = 0;

boutons.forEach(function(bouton) {
    let valeur = Math.floor(Math.random() * 4) + 1;
    bouton.querySelector("span").textContent = valeur;
    total += valeur;
});

document.querySelector("#total span").textContent = total;

boutons.forEach(function(bouton) {
    bouton.addEventListener("click", function() {
        let span = bouton.querySelector("span");
        let compteur = parseInt(span.textContent);

        if (compteur > 0) {
            let src = bouton.querySelector("img").src;
            document.getElementById("main").innerHTML += '<img src="' + src + '">';
            compteur--;
            span.textContent = compteur;
            if (compteur === 0) {
                bouton.classList.add("vide");
            }
            total--;
            document.querySelector("#total span").textContent = total;
            if (total === 0) {
                document.getElementById("total").classList.add("vide");
            }    
        }
    });
});
});