// script.js
let currentIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.slide');
    if (index >= slides.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = slides.length - 1;
    } else {
        currentIndex = index;
    }
    const offset = -currentIndex * 100;
    document.querySelector('.slides').style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}

document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentIndex);
    setInterval(nextSlide, 5000); // Cambia de imagen cada 5 segundos
});



// Obtener elementos del DOM
const modal = document.getElementById("loginModal");
const btns = document.querySelectorAll(".ver-producto");
const span = document.getElementsByClassName("close")[0];

// Mostrar la ventana modal al hacer clic en cualquier enlace "Ver Producto"
btns.forEach(btn => {
    btn.onclick = function(event) {
        event.preventDefault();
        modal.style.display = "block";
    }
});

// Cerrar la ventana modal al hacer clic en la 'x'
span.onclick = function() {
    modal.style.display = "none";
}

// Cerrar la ventana modal al hacer clic fuera de ella
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
