document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('ajouter').addEventListener('click', function() {
        let nom = document.getElementById('nom').value;
        let couleur = document.getElementById('couleur').value;
        let figure = document.createElement('figure');
        figure.className = 'chat';
        figure.innerHTML = '<img src="img/' + couleur + '.jpg" alt=""><figcaption>' + nom + '</figcaption>';
        document.getElementById('chats').appendChild(figure);
        document.getElementById('nom').value = '';
        document.getElementById('ajouter').disabled = true;
        document.getElementById('vider').disabled = false;
        document.getElementById('nombre').textContent = document.querySelectorAll('#chats figure').length;
    });

    document.getElementById('nom').addEventListener('input', function() {
        let nom = this.value;
        if (nom === '') {
            document.getElementById('ajouter').disabled = true;
        } else {
            document.getElementById('ajouter').disabled = false;
            document.querySelectorAll('.chat').forEach(function(chat) {
                chat.classList.remove('hola');
                if (chat.querySelector('figcaption').textContent === nom) {
                    chat.classList.add('hola');
                }
            });
        }
    });

    document.getElementById('vider').addEventListener('click', function() {
        document.getElementById('chats').innerHTML = '';
        document.getElementById('nombre').textContent = 0;
        document.getElementById('vider').disabled = true;
    });
});
