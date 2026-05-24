$(function() {
    function piocher() {
        let total = 0;
        $('.jeton').each(function() {
            if ($(this).hasClass('libre')) {
                let valeur = Math.floor(Math.random() * 9) + 1;
                $(this).text(valeur);
            }
            total += parseInt($(this).text());
        });
        $('#total').text(total);

        if (total >= 44) {
            $('#victoire').fadeIn();
        }
    }

    piocher();

    $('#plateau').on('click', '.jeton', function() {
        $(this).toggleClass('libre');
    });

    let cartouche = 1;
    $('#pioche').on('click', function() {
        if (cartouche > 5) return;

        $('#c' + cartouche).addClass('vide');
        cartouche++;

        piocher();

        if (cartouche > 5 && parseInt($('#total').text()) < 44) {
            $('#perdu').fadeIn();
        }
    });
});
