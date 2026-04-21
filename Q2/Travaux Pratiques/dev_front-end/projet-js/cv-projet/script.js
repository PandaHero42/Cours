// 1. SWIPER - autoplay désactivé sur mobile
var certSwiper = new Swiper('.cert-swiper', {
    loop: true,
    autoplay: { delay: 3000, disableOnInteraction: false },
    pagination: {
        el: '.swiper-pagination',
        clickable: true
    },
    speed: 600
});

$(document).ready(function () {

    // 2. TYPED.JS - effet de frappe 
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

    //  3. INTERSECTION OBSERVER - scroll pour reveal les sections 

    var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.sb-section, .mc-section').forEach(function (el) {
        revealObserver.observe(el);
    });

    //  4. INTERSECTION OBSERVER - animation barres de compétences 
    var skillsDone = false;
    var skillObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting && !skillsDone) {
                skillsDone = true;
                $('.skill-fill').each(function () {
                    $(this).animate({ width: $(this).data('width') + '%' }, 900);
                });
                skillObserver.disconnect();
            }
        });
    }, { threshold: 0.3 });

    var skillSection = document.querySelector('.skill-fill');
    if (skillSection) skillObserver.observe(skillSection.closest('.sb-section'));

    //  5. PARTICLES.JS - fond animé dans le header 
    var nightParticles = {
        particles: {
            number: { value: 70, density: { enable: true, value_area: 800 } },
            color: { value: ['#06b6d4', '#8b5cf6'] },
            shape: {
                type: 'polygon',
                polygon: { nb_sides: 6 }
            },
            opacity: { value: 0.85, random: true, anim: { enable: true, speed: 0.8, opacity_min: 0.4, sync: false } },
            size: { value: 5, random: true },
            line_linked: {
                enable: true,
                distance: 140,
                color: '#8b5cf6',
                opacity: 0.55,
                width: 1
            },
            move: { enable: true, speed: 1.5, random: true, out_mode: 'bounce' }
        },
        interactivity: {
            detect_on: 'canvas',
            events: { onhover: { enable: true, mode: 'grab' }, onclick: { enable: false } },
            modes: { grab: { distance: 140, line_linked: { opacity: 0.9 } } }
        },
        retina_detect: true
    };

    var dayParticles = {
        particles: {
            number: { value: 140, density: { enable: true, value_area: 800 } },
            color: { value: ['#9c6644', '#7d5a44', '#c49a6c'] },
            shape: { type: 'triangle' },
            opacity: { value: 0.7, random: true, anim: { enable: true, speed: 0.6, opacity_min: 0.3, sync: false } },
            size: { value: 6, random: true },
            line_linked: { enable: false },
            move: { enable: true, speed: 1.2, random: true, out_mode: 'out', direction: 'top' }
        },
        interactivity: {
            detect_on: 'canvas',
            events: { onhover: { enable: true, mode: 'repulse' }, onclick: { enable: false } },
            modes: { repulse: { distance: 80 } }
        },
        retina_detect: true
    };

    function initParticles(isNightMode) {
        if (!document.getElementById('particles-js')) return;
        if (window.pJSDom && window.pJSDom.length > 0) {
            try {
                window.pJSDom[0].pJS.fn.vendors.destroypJS();
            } catch (e) {}
            window.pJSDom = [];
        }
        setTimeout(function () {
            particlesJS('particles-js', isNightMode ? nightParticles : dayParticles);
        }, 50);
    }

    //  6. DARK / LIGHT MODE 
    var isDark = true;

    setTimeout(function () { initParticles(true); }, 100);

    //  7. RESIZE - relancer particles si nécessaire 
    var resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            if (!window.pJSDom || window.pJSDom.length === 0) {
                initParticles(isDark);
            }
        }, 200);
    });
    $('#darkModeBtn').on('click', function () {
        isDark = !isDark;
        $('body').toggleClass('light', !isDark);
        $(this).find('i')
            .toggleClass('fa-sun', isDark)
            .toggleClass('fa-moon', !isDark);
        initParticles(isDark);
    });

    //  8. BOUTON IMPRESSION 
    $('#printBtn').on('click', function () {
        window.print();
    });

});
