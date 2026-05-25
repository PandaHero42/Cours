document.addEventListener("DOMContentLoaded", function() {
    let grille = document.getElementById('grille');

    for (let i = 0; i < 81; i++) {
        let valeur = (Math.floor(Math.random() * 7) + 1) * (Math.floor(Math.random() * 7) + 1);
        let div = document.createElement('div');
        div.className = 'case';
        div.textContent = valeur;
        grille.appendChild(div);
    }

    grille.addEventListener('mouseover', function(e) {
        if (!e.target.classList.contains('case')) return;
        let valeur = parseInt(e.target.textContent);

        document.querySelectorAll('.case').forEach(function(c) {
            c.classList.remove('moiaussi');
            if (parseInt(c.textContent) === valeur) c.classList.add('moiaussi');
        });

        let nb = 0;
        [2, 3, 5, 7].forEach(function(n) {
            let div = document.getElementById('div' + n);
            if (valeur % n === 0) { div.classList.add('vert'); nb++; }
            else { div.classList.remove('vert'); }
        });

        document.getElementById('nb').textContent = nb;
        document.getElementById('metre').style.width = (nb * 25) + '%';
    });

    grille.addEventListener('mouseleave', function() {
        document.querySelectorAll('.case').forEach(c => c.classList.remove('moiaussi'));
        [2, 3, 5, 7].forEach(n => document.getElementById('div' + n).classList.remove('vert'));
        document.getElementById('nb').textContent = 0;
        document.getElementById('metre').style.width = '0%';
    });
});
