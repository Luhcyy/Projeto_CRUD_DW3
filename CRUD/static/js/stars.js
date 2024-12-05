document.querySelectorAll('.stars input').forEach((input) => {
    input.addEventListener('change', (event) => {
        const rating = event.target.value;
        console.log('Rating selecionado: ' + rating);  
    });
});
