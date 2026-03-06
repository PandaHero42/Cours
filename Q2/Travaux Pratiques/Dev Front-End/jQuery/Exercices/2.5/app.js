$(document).ready(function () {

  // Étape 2 : rendre invisibles les éléments apparition
  $(".apparition").addClass("invisible");

  function checkVisibility() {

    const scrollTop = $(window).scrollTop();
    const windowHeight = $(window).height();
    const windowBottom = scrollTop + windowHeight;

    $(".apparition.invisible").each(function () {

      const elTop = $(this).offset().top;
      const elHeight = $(this).outerHeight();
      const threshold = elTop + (elHeight / 2);

      if (windowBottom >= threshold) {
        $(this).removeClass("invisible");
      }

    });
  }

  $(window).on("scroll", checkVisibility);

  // vérifie aussi au chargement
  checkVisibility();

});