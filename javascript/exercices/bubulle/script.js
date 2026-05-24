$(function() {
    $('#menu a').on('mouseenter', function() {
        let pos = $(this).position();
        let largeur = $(this).outerWidth();

        $('#bubulle').animate({
            left: pos.left,
            width: largeur
        }, 200);
    });
});