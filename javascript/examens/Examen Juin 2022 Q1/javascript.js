document.addEventListener("DOMContentLoaded", function() {
    let contenances = [8, 10, 12, 15, 20];
    let dechets = ['planches', 'bricaillons', 'briques', 'carrelages', 'poutres', 'sable', 'contreplaqués'];

    function evaluer() {
        for (let i = 1; i <= 4; i++) {
            let total = 0;
            document.querySelectorAll('#conteneur' + i + ' .dechet').forEach(function(d) {
                total += parseInt(d.dataset.volume);
            });
            let contenance = parseInt(document.querySelector('#conteneur' + i + '-etiquette .contenance').textContent);
            let contenuEl = document.querySelector('#conteneur' + i + '-etiquette .contenu');
            contenuEl.textContent = total;
            if (total > contenance) contenuEl.classList.add('trop');
            else contenuEl.classList.remove('trop');
        }
    }

    for (let i = 1; i <= 4; i++) {
        let contenance = contenances[Math.floor(Math.random() * contenances.length)];
        document.querySelector('#conteneur' + i + '-etiquette .contenance').textContent = contenance;

        let nbDechets = Math.floor(Math.random() * 5) + 1;
        for (let j = 0; j < nbDechets; j++) {
            let nom = dechets[Math.floor(Math.random() * dechets.length)];
            let volume = Math.floor(Math.random() * 7) + 1;
            let div = document.createElement('div');
            div.className = 'dechet';
            div.dataset.volume = volume;
            div.textContent = nom + ' (' + volume + 'L)';
            document.getElementById('conteneur' + i).appendChild(div);
        }
    }

    evaluer();

    document.getElementById('main').addEventListener('click', function(e) {
        if (e.target.classList.contains('dechet')) {
            e.target.remove();
            evaluer();
        }
    });
});
