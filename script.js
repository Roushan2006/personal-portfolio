/* ── NAVBAR SCROLL SHADOW ─────────────────────────── */
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 30);
});

/* ── HAMBURGER MENU ───────────────────────────────── */
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        navLinks.classList.remove('open');
    });
});

/* ── ACTIVE NAV LINK ──────────────────────────────── */
const sections = document.querySelectorAll('section[id]');
const allLinks = document.querySelectorAll('.nav-link');

function activateLink() {

    let current = '';

    sections.forEach(sec => {
        const sectionTop = sec.offsetTop - 140;

        if (scrollY >= sectionTop) {
            current = sec.getAttribute('id');
        }
    });

    allLinks.forEach(link => {
        link.classList.remove('active');

        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', activateLink);

/* ── SMOOTH SCROLL ────────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener('click', function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));

        target.scrollIntoView({
            behavior: 'smooth'
        });

    });

});

/* ── SCROLL REVEAL ANIMATION ─────────────────────── */
const revealObserver = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);

        }

    });

}, {
    threshold: 0.15
});

document.querySelectorAll('.reveal, .reveal-up').forEach(el => {
    revealObserver.observe(el);
});

/* ── ANIMATED COUNTERS ───────────────────────────── */
const counterObserver = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (!entry.isIntersecting) return;

        const el = entry.target;
        const target = +el.dataset.target;

        let current = 0;

        const updateCounter = () => {

            const increment = target / 70;

            if (current < target) {

                current += increment;
                el.innerText = Math.ceil(current) + '+';

                requestAnimationFrame(updateCounter);

            } else {

                el.innerText = target + '+';

            }

        };

        updateCounter();

        counterObserver.unobserve(el);

    });

}, {
    threshold: 0.5
});

document.querySelectorAll('.stat-num').forEach(counter => {
    counterObserver.observe(counter);
});

/* ── HERO TAG STAGGER ────────────────────────────── */
document.querySelectorAll('.hero-tags .tag').forEach((tag, i) => {

    tag.style.opacity = '0';
    tag.style.transform = 'translateY(20px)';

    setTimeout(() => {

        tag.style.transition = '0.5s ease';
        tag.style.opacity = '1';
        tag.style.transform = 'translateY(0)';

    }, 300 + (i * 100));

});

/* ── MAGNETIC BUTTON EFFECT ───────────────────────── */
document.querySelectorAll('.contact-btn').forEach(button => {

    button.addEventListener('mousemove', e => {

        const rect = button.getBoundingClientRect();

        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        button.style.transform = `
            translate(${x * 0.2}px, ${y * 0.2}px)
            scale(1.05)
        `;

    });

    button.addEventListener('mouseleave', () => {

        button.style.transform = 'translate(0px,0px) scale(1)';

    });

});

/* ── 3D CARD EFFECT ───────────────────────────────── */
document.querySelectorAll('.project-card, .skill-card').forEach(card => {

    card.addEventListener('mousemove', e => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / 18);
        const rotateY = ((centerX - x) / 18);

        card.style.transform = `
            perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            scale(1.04)
        `;

    });

    card.addEventListener('mouseleave', () => {

        card.style.transform = `
            perspective(1000px)
            rotateX(0deg)
            rotateY(0deg)
            scale(1)
        `;

    });

});

/* ── CUSTOM CURSOR GLOW ───────────────────────────── */
const glow = document.createElement('div');

glow.classList.add('cursor-glow');

document.body.appendChild(glow);

document.addEventListener('mousemove', e => {

    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';

});

/* ── FLOATING PARTICLES ───────────────────────────── */
const particleContainer = document.createElement('div');
particleContainer.classList.add('particles');

document.body.appendChild(particleContainer);

for (let i = 0; i < 35; i++) {

    const particle = document.createElement('span');

    particle.classList.add('particle');

    particle.style.left = Math.random() * 100 + 'vw';
    particle.style.animationDuration = 5 + Math.random() * 10 + 's';
    particle.style.animationDelay = Math.random() * 5 + 's';

    particleContainer.appendChild(particle);

}

/* ── TYPING EFFECT ────────────────────────────────── */
const typingText = document.querySelector('.typing-text');

if (typingText) {

    const words = [
        'Full Stack Developer',
        'AI Enthusiast',
        'UI/UX Designer',
        'Java Programmer'
    ];

    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function typeEffect() {

        const currentWord = words[wordIndex];

        if (!isDeleting) {

            typingText.textContent =
                currentWord.substring(0, charIndex++);

            if (charIndex > currentWord.length) {

                isDeleting = true;

                setTimeout(typeEffect, 1200);
                return;
            }

        } else {

            typingText.textContent =
                currentWord.substring(0, charIndex--);

            if (charIndex < 0) {

                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;

            }

        }

        setTimeout(typeEffect, isDeleting ? 50 : 100);

    }

    typeEffect();

}

/* ── PARALLAX EFFECT ──────────────────────────────── */
window.addEventListener('mousemove', e => {

    document.querySelectorAll('.parallax').forEach(layer => {

        const speed = layer.dataset.speed || 3;

        const x = (window.innerWidth - e.pageX * speed) / 100;
        const y = (window.innerHeight - e.pageY * speed) / 100;

        layer.style.transform = `translate(${x}px, ${y}px)`;

    });

});

/* ── PRELOADER ────────────────────────────────────── */
window.addEventListener('load', () => {

    const loader = document.querySelector('.loader');

    if (loader) {

        loader.style.opacity = '0';

        setTimeout(() => {
            loader.style.display = 'none';
        }, 500);

    }

});