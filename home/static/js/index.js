// index.js

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Parallax effect for hero section
    const heroContent = document.querySelector('.hero-content');
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        heroContent.style.transform = `translateY(${scrolled * 0.4}px)`;
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe service items
    document.querySelectorAll('.service-item').forEach(item => {
        observer.observe(item);
    });

    // Video loading optimization
    const video = document.querySelector('.hero-bg-video');
    if (video) {
        video.playbackRate = 0.75; // Slightly slower playback for smoother appearance
        
        // Pause video when not in viewport to save resources
        let videoObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    video.play();
                } else {
                    video.pause();
                }
            });
        }, { threshold: 0 });
        
        videoObserver.observe(video);
    }
});

// Trusted By Section Animations
document.addEventListener('DOMContentLoaded', function() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    };

    const logoItems = document.querySelectorAll('.logo-item');
    
    // Add stagger delay to each logo
    logoItems.forEach((item, index) => {
        item.style.transitionDelay = `${index * 100}ms`;
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Add hover animation after logo appears
                setTimeout(() => {
                    entry.target.style.transform = 'translateY(-5px)';
                    setTimeout(() => {
                        entry.target.style.transform = 'translateY(0)';
                    }, 200);
                }, parseFloat(entry.target.style.transitionDelay) + 300);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe each logo item
    logoItems.forEach(item => {
        observer.observe(item);
    });

    // Optional: Add logo shuffle animation on interval
    let isAnimating = false;
    
    function shuffleLogos() {
        if (isAnimating) return;
        isAnimating = true;

        const logos = document.querySelector('.trusted-logos');
        const items = Array.from(logos.children);
        
        items.forEach((item, i) => {
            item.style.transition = 'all 0.5s ease';
            item.style.transform = 'scale(0.95) translateY(10px)';
            item.style.opacity = '0.5';
            
            setTimeout(() => {
                item.style.transform = 'scale(1) translateY(0)';
                item.style.opacity = '1';
            }, i * 100 + 300);
        });

        setTimeout(() => {
            isAnimating = false;
        }, items.length * 100 + 800);
    }

    // Shuffle logos every 8 seconds
    setInterval(shuffleLogos, 8000);
});