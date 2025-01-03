/* static/js/gallery.js */
let currentImageIndex = 0;
let autoPlayInterval;
const autoPlayDelay = 2000; // 5 seconds

function openLightbox(index) {
    currentImageIndex = index;
    updateLightboxImage();
    document.getElementById('lightbox').style.display = 'block';
    startAutoPlay();
}

function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
    stopAutoPlay();
}

function changeImage(direction) {
    currentImageIndex = (currentImageIndex + direction + galleryImages.length) % galleryImages.length;
    updateLightboxImage();
    restartAutoPlay();
}

function updateLightboxImage() {
    const image = galleryImages[currentImageIndex];
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxDescription = document.getElementById('lightbox-description');
    
    // Add fade effect
    lightboxImg.style.opacity = '0';
    setTimeout(() => {
        lightboxImg.src = image.url;
        lightboxImg.alt = image.title;
        lightboxTitle.textContent = image.title;
        lightboxDescription.textContent = image.description;
        lightboxImg.style.opacity = '1';
    }, 300);
}

function startAutoPlay() {
    autoPlayInterval = setInterval(() => {
        changeImage(1);
    }, autoPlayDelay);
}

function stopAutoPlay() {
    clearInterval(autoPlayInterval);
}

function restartAutoPlay() {
    stopAutoPlay();
    startAutoPlay();
}

// Close lightbox when clicking outside the image
document.getElementById('lightbox').addEventListener('click', function(e) {
    if (e.target === this) {
        closeLightbox();
    }
});

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    if (document.getElementById('lightbox').style.display === 'block') {
        if (e.key === 'ArrowLeft') {
            changeImage(-1);
        } else if (e.key === 'ArrowRight') {
            changeImage(1);
        } else if (e.key === 'Escape') {
            closeLightbox();
        }
    }
});