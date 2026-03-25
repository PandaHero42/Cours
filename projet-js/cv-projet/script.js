$(document).ready(function () {

    // TYPED.JS — effet de frappe 
    new Typed('#typed-output', {
        strings: [
            'Étudiant en informatique',
            'Réseaux &amp; Télécommunications',
            'Cybersécurité',
            'Administration Systèmes'
        ],
        typeSpeed: 50,
        backSpeed: 30,
        backDelay: 1800,
        loop: true,
        smartBackspace: true
    });

    // ===== 2. WAYPOINTS — apparition des sections sidebar =====
    $('.sb-section').each(function (i) {
        var $el = $(this);
        if (this.getBoundingClientRect().top < window.innerHeight * 0.92) {
            setTimeout(function () { $el.addClass('visible'); }, i * 100);
            return;
        }
        new Waypoint({
            element: this,
            handler: function () { $el.addClass('visible'); this.destroy(); },
            offset: '92%'
        });
    });

    // ===== 3. WAYPOINTS — apparition des sections principales =====
    $('.mc-section').each(function (i) {
        var $el = $(this);
        if (this.getBoundingClientRect().top < window.innerHeight * 0.92) {
            setTimeout(function () { $el.addClass('visible'); }, i * 100);
            return;
        }
        new Waypoint({
            element: this,
            handler: function () { $el.addClass('visible'); this.destroy(); },
            offset: '92%'
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

    var $skillSection = $('.skill-fill').first().closest('.sb-section');
    if ($skillSection.length && $skillSection[0].getBoundingClientRect().top < window.innerHeight) {
        animateSkills();
    } else {
        new Waypoint({
            element: $skillSection[0],
            handler: function () { animateSkills(); this.destroy(); },
            offset: '90%'
        });
    }

    // ===== 5. DARK / LIGHT MODE =====
    var isDark = true;
    $('#darkModeBtn').on('click', function () {
        isDark = !isDark;
        $('body').toggleClass('light', !isDark);
        $(this).find('i')
            .toggleClass('fa-sun', isDark)
            .toggleClass('fa-moon', !isDark);
    });

    // ===== 6. BOUTON IMPRESSION =====
    $('#printBtn').on('click', function () {
        window.print();
    });

});
