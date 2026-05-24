$(function() {
    $('#ajouter').on('click', function() {
        let nom = $('#nom').val();
        let couleur = $('#couleur').val();
        $('#chats').append('<figure class="chat"><img src="img/' + couleur + '.jpg" alt=""><figcaption>' + nom + '</figcaption></figure>');
        $('#nom').val('');
        $('#ajouter').attr('disabled', true);
        $('#vider').attr('disabled', false);
        $('#nombre').text($('#chats figure').length);
    });
    $('#nom').on('input', function() {
        let nom = $(this).val();
        if (nom === '') {
            $('#ajouter').attr('disabled', true);
        } else {
            $('#ajouter').attr('disabled', false);
            $('.chat').removeClass('hola');
            $('.chat').each(function() {
                if ($('figcaption', this).text() === nom) {
                    $(this).addClass('hola');
                }
        });
        }
        
    });
    $('#vider').on('click', function() {
        $('#chats').empty();
        $('#nombre').text(0);
        $('#vider').attr('disabled', true);
    })
});