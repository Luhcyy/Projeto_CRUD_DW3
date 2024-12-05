const menuToggle = document.getElementById('menu-toggle');
const hiddenMenu = document.getElementById('hidden-menu');

menuToggle.addEventListener('click', (e) => {
    e.preventDefault(); 
    hiddenMenu.classList.toggle('active');
    e.stopPropagation(); 
});

document.addEventListener('click', (e) => {

    if (hiddenMenu.classList.contains('active') && !hiddenMenu.contains(e.target)) {
        hiddenMenu.classList.remove('active'); 
    }
});
