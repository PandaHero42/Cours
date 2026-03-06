// On attend que jQuery soit dispo (local OU CDN fallback)
function startApp() {
  console.log("jQuery OK:", $.fn.jquery);

  // ===== LIGHTBOX =====
  function openLightbox(src) {
    $("#lightImg").attr("src", src);
    $("#lightbox").addClass("show").hide().fadeIn(250);
    $("body").css("overflow", "hidden"); // bloque le scroll
  }

  function closeLightbox() {
    $("#lightbox").fadeOut(250, function () {
      $("#lightbox").removeClass("show");
      $("#lightImg").attr("src", "");
    });
    $("body").css("overflow", "auto");
  }

  // clic sur une vignette (figure entière)
  $("figure").on("click", function () {
    const src = $(this).find("img").attr("src");
    openLightbox(src);
  });

  // fermeture : clic sur fond noir OU sur la croix
  $("#lightbox").on("click", function (e) {
    if (e.target.id === "lightbox") {
      closeLightbox();
    }
  });

  $("#close").on("click", function (e) {
    e.stopPropagation();
    closeLightbox();
  });

  // fermeture : touche ESC
  $(document).on("keydown", function (e) {
    if (e.key === "Escape") {
      closeLightbox();
    }
  });

  // ===== VOLET NAV =====
  $("#burger").on("click", function (e) {
    e.stopPropagation();          // IMPORTANT pour ne pas fermer direct
    $("#volet").toggleClass("open");
  });

  // clic n’importe où (document) ferme le volet
  $(document).on("click", function () {
    $("#volet").removeClass("open");
  });

  // clic dans le volet ne ferme pas (optionnel mais agréable)
  $("#volet").on("click", function (e) {
    e.stopPropagation();
  });
}

// Si jQuery est déjà là
if (window.jQuery) {
  $(document).ready(startApp);
} else {
  // Sinon, on attend un peu que le CDN se charge (fallback)
  const timer = setInterval(function () {
    if (window.jQuery) {
      clearInterval(timer);
      $(document).ready(startApp);
    }
  }, 50);
}