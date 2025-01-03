
document.addEventListener('DOMContentLoaded', () => {
    // Add parallax effect to hero section
    const hero = document.querySelector('.about-hero');
    window.addEventListener('scroll', () => {
        let offset = window.scrollY * 0.5;
        hero.style.backgroundPositionY = `${offset}px`;
    });

    // Fade-in effects for each section
    const sections = document.querySelectorAll('section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    sections.forEach(section => {
        section.classList.add('fade-out');
        observer.observe(section);
    });
});

