$(function() {
    $('#burger').on('click', function(e) {
        e.stopPropagation();
        $('#volet').toggleClass('ouvert');
    });
    $(document).on('click', function() {
        $('#volet').removeClass('ouvert');
    });
    $('#galerie figure').on('click', function() {
        let src = $(this).find('img').attr('src');
        $('#lightbox img').attr('src', src);
        $('#lightbox').fadeIn();
    });
    $('#lightbox').on('click', function() {
        $(this).fadeOut();
    });
    $(document).on('keydown', function(e) {
        if (e.key === 'Escape') {
            $('#lightbox').fadeOut();
        }
    });
});