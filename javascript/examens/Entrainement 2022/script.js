$(function() {
    for (let i = 0; i < 81; i++) {
        let valeur = (Math.floor(Math.random() * 7) + 1) * (Math.floor(Math.random() * 7) + 1);
        $('#grille').append('<div class="case">' + valeur + '</div>');
    }
    $('#grille').on('mouseover', '.case', function() {
        let valeur = parseInt($(this).text());
        $('.case').removeClass('moiaussi');
        $('.case').each(function() {
            if (parseInt($(this).text()) === valeur) {
                $(this).addClass('moiaussi');
            }
        });

        let nb = 0;
        if (valeur % 2 === 0) {
            $('#div2').addClass('vert');
            nb++;
        } else {
            $('#div2').removeClass('vert');
        }
        if (valeur % 3 === 0) {
            $('#div3').addClass('vert');
            nb++;
        } else {
            $('#div3').removeClass('vert');
        }
        if (valeur % 5 === 0) {
            $('#div5').addClass('vert');
            nb++;
        } else {
            $('#div5').removeClass('vert');
        }
        if (valeur % 7 === 0) {
            $('#div7').addClass('vert');
            nb++;
        } else {
            $('#div7').removeClass('vert');
        }
        $('#nb').text(nb);
        $('#metre').animate({width: (nb * 25) + '%'}, 300);
    });
    $('#grille').on('mouseleave', function() {
        $('.case').removeClass('moiaussi');
        $('#div2, #div3, #div5, #div7').removeClass('vert');
        $('#nb').text(0);
        $('#metre').animate({width: '0%'}, 300);
    });
});