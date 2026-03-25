const nameInput = document.getElementById("name");

function majPremiereLettre() {
    const value = nameInput.value;

    // Sécurité : si le champ est vide

    if (value.length === 0) {
        return;
    }

    const firstLetter = value.charAt(0).toUpperCase();
    const rest = value.slice(1);

    const result = firstLetter + rest;
    nameInput.value = result;

    console.log("Avant :", value);
    console.log("Après :", result);
}

nameInput.addEventListener("blur", majPremiereLettre);

