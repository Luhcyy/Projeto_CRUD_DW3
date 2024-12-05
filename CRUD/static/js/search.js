const searchInput = document.getElementById('search-input');
const clearButton = document.getElementById('clear-button');
const searchForm = document.querySelector('.search-bar'); 

searchInput.addEventListener('input', () => {
    clearButton.style.visibility = searchInput.value ? 'visible' : 'hidden';
});

clearButton.addEventListener('click', (event) => {
    event.preventDefault(); 
    searchInput.value = ''; 
    clearButton.style.visibility = 'hidden'; 
    searchInput.focus(); 
});

searchForm.addEventListener('submit', (event) => {
    if (!searchInput.value) {
        event.preventDefault(); 
    }
});
