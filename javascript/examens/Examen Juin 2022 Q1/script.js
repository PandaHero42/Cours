$(function() {
    let contenances = [8, 10, 12, 15, 20];
    let dechets = ['planches', 'bricaillons', 'briques', 'carrelages', 'poutres', 'sable', 'contreplaqués'];

    function evaluer() {
        for (let i = 1; i <= 4; i++) {
            let total = 0;
            $('#conteneur' + i + ' .dechet').each(function() {
                total += parseInt($(this).data('volume'));
            });
            let contenance = parseInt($('#conteneur' + i + '-etiquette .contenance').text());
            $('#conteneur' + i + '-etiquette .contenu').text(total);
            if (total > contenance) {
                $('#conteneur' + i + '-etiquette .contenu').addClass('trop');
            } else {
                $('#conteneur' + i + '-etiquette .contenu').removeClass('trop');
            }
        }
    }
    for (let i = 1; i <= 4; i++) {
        let contenance = contenances[Math.floor(Math.random() * contenances.length)];
        $('#conteneur' + i + '-etiquette .contenance').text(contenance);

        let nbDechets = Math.floor(Math.random() * 5) + 1;
        for (let j = 0; j < nbDechets; j++) {
            let nom = dechets[Math.floor(Math.random() * dechets.length)];
            let volume = Math.floor(Math.random() * 7) + 1;
            $('#conteneur' + i).append('<div class="dechet" data-volume="' + volume + '">' + nom + ' (' + volume + 'L)</div>');
        }
    }
    evaluer();
    $('#main').on('click', '.dechet', function() {
      $(this).remove();
      evaluer();
    });    
});