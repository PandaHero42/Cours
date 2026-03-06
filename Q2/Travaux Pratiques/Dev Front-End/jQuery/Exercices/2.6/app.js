$(document).ready(function () {

  $(window).on("scroll", function () {
    const scrollTop = $(window).scrollTop();

    // facteur = vitesse du background (0.3 = bouge moins vite que la page)
    const y = -(scrollTop * 0.3);

    $(".hero").css("background-position", "center " + y + "px");
  });

});