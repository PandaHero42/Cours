$(document).ready(function () {

    // ===== 1. TYPED.JS — effet de frappe sur le sous-titre =====
    new Typed('#typed-subtitle', {
        strings: [
            'Réseaux &amp; Télécommunications',
            'Cybersécurité',
            'Administration Systèmes'
        ],
        typeSpeed: 60,
        backSpeed: 40,
        backDelay: 2200,
        loop: true
    });

    // ===== 2. WAYPOINTS — apparition des blocs sidebar au scroll =====
    $('.sb-section').each(function (i) {
        var $el = $(this);
        if (this.getBoundingClientRect().top < window.innerHeight * .92) {
            setTimeout(function () { $el.addClass('visible'); }, i * 100);
            return;
        }
        new Waypoint({
            element: this,
            handler: function () { $el.addClass('visible'); this.destroy(); },
            offset: '92%'
        });
    });

    // ===== 3. WAYPOINTS — apparition des blocs principaux au scroll =====
    $('.mc-section').each(function (i) {
        var $el = $(this);
        if (this.getBoundingClientRect().top < window.innerHeight * .92) {
            setTimeout(function () { $el.addClass('visible'); }, i * 120);
            return;
        }
        new Waypoint({
            element: this,
            handler: function () { $el.addClass('visible'); this.destroy(); },
            offset: '90%'
        });
    });

    // ===== 4. SKILL BARS — animation jQuery =====
    var skillsDone = false;
    function animateSkills() {
        if (skillsDone) return;
        skillsDone = true;
        $('.skill-fill').each(function () {
            $(this).animate({ width: $(this).data('width') + '%' }, 900);
        });
    }

    var $firstSb = $('.skill-fill').first().closest('.sb-section');
    if ($firstSb[0].getBoundingClientRect().top < window.innerHeight) {
        animateSkills();
    } else {
        new Waypoint({
            element: $firstSb[0],
            handler: function () { animateSkills(); this.destroy(); },
            offset: '90%'
        });
    }

    // ===== 5. DARK MODE =====
    var isDark = false;
    $('#darkModeBtn').on('click', function () {
        isDark = !isDark;
        $('body').toggleClass('dark', isDark);
        $(this).find('i')
            .toggleClass('fa-moon', !isDark)
            .toggleClass('fa-sun', isDark);
    });

    // ===== 6. BOUTON IMPRESSION =====
    $('#printBtn').on('click', function () {
        window.print();
    });

});
