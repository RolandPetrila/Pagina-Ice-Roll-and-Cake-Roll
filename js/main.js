// Lightbox pentru imagini
document.querySelectorAll('.gallery img').forEach(img => {
    img.addEventListener('click', () => {
        const lightbox = document.createElement('div');
        lightbox.classList.add('lightbox');
        lightbox.innerHTML = `<img src="${img.src}" alt="${img.alt}">`;
        document.body.appendChild(lightbox);

        lightbox.addEventListener('click', () => {
            document.body.removeChild(lightbox);
        });
    });
});

// Lazy loading pentru imagini
document.querySelectorAll('.gallery img').forEach(img => {
    img.loading = 'lazy';
});