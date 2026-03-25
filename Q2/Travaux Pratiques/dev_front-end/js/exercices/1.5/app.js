function buildEmails() {
    const emails = document.querySelectorAll(".email");

    emails.forEach(email => {
        if (email.classList.contains("std")) {
            email.innerText += "@std.heh.be";
        } else {
            email.innerText += "@heh.be";
        }
    });
}

// Après chargement complet de la page 

window.addEventListener("load", () => {
    setTimeout(buildEmails, 300);
})