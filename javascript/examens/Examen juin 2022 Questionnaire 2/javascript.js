document.addEventListener("DOMContentLoaded", function() {
    let formes = ["triangle", "cercle", "carré", "pentagone", "trapèze", "parallélogramme", "losange", "octogone"];
    let laForme;

    function genererLigne() {
        let ligne = document.createElement('div');
        ligne.className = 'ligne';

        let formesDeLaLigne = [];
        for (let i = 0; i < 8; i++) {
            formesDeLaLigne.push(formes[Math.floor(Math.random() * formes.length)]);
        }
        if (!formesDeLaLigne.includes(laForme)) {
            formesDeLaLigne[Math.floor(Math.random() * 8)] = laForme;
        }

        formesDeLaLigne.forEach(function(f) {
            let div = document.createElement('div');
            div.className = 'forme ' + f;
            ligne.appendChild(div);
        });

        document.getElementById('main').prepend(ligne);
    }

    laForme = formes[Math.floor(Math.random() * formes.length)];
    document.getElementById('laforme').textContent = laForme;
    genererLigne();

    document.getElementById('main').addEventListener('click', function(e) {
        if (!e.target.classList.contains('forme')) return;
        if (e.target.classList.contains(laForme)) {
            e.target.classList.add('goodjob');
            if (document.querySelectorAll('.' + laForme + ':not(.goodjob)').length === 0) {
                genererLigne();
            }
        } else {
            e.target.classList.add('badjob');
        }
    });
});
