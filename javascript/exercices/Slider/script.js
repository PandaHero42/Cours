$(function() {

let index = 0;

setInterval(function() {
    index++;
    if (index > 5) index = 0;

    $('#plateau').animate({ top: -index * 600 }, 500);
    $('#num').text(index + 1);
}, 3000);

});