$(function() {
    let formes = ["triangle", "cercle", "carré", "pentagone", "trapèze", "parallélogramme", "losange", "octogone"];
    let laForme;

    function genererLigne() {
        let ligne = $('<div class="ligne"></div>');

        let formesDeLaLigne = [];
        for (let i = 0; i < 8; i++) {
            formesDeLaLigne.push(formes[Math.floor(Math.random() * formes.length)]);
        }

        if (!formesDeLaLigne.includes(laForme)) {
            formesDeLaLigne[Math.floor(Math.random() * 8)] = laForme;
        }

        formesDeLaLigne.forEach(function(f) {
            ligne.append('<div class="forme ' + f + '"></div>');
        });
        $('#main').prepend(ligne);
    }

    laForme = formes[Math.floor(Math.random() * formes.length)];
    $('#laforme').text(laForme);
    genererLigne();

    $('#main').on('click', '.forme', function() {
        if ($(this).hasClass(laForme)) {
            $(this).addClass('goodjob');

            if ($('.' + laForme).not('.goodjob').length === 0) {
                genererLigne();
            }
        } else {
            $(this).addClass('badjob');
        }
    });
});