document.addEventListener("DOMContentLoaded", function() {
    function piocher() {
        let total = 0;
        document.querySelectorAll('.jeton').forEach(function(jeton) {
            if (jeton.classList.contains('libre')) {
                jeton.textContent = Math.floor(Math.random() * 9) + 1;
            }
            total += parseInt(jeton.textContent);
        });
        document.getElementById('total').textContent = total;

        if (total >= 44) {
            document.getElementById('victoire').style.display = 'block';
        }
    }

    piocher();

    document.getElementById('plateau').addEventListener('click', function(e) {
        if (e.target.classList.contains('jeton')) {
            e.target.classList.toggle('libre');
        }
    });

    let cartouche = 1;
    document.getElementById('pioche').addEventListener('click', function() {
        if (cartouche > 5) return;
        document.getElementById('c' + cartouche).classList.add('vide');
        cartouche++;
        piocher();
        if (cartouche > 5 && parseInt(document.getElementById('total').textContent) < 44) {
            document.getElementById('perdu').style.display = 'block';
        }
    });
});
