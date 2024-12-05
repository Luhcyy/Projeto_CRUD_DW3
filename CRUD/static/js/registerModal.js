function showModal() {
    const modal = document.getElementById('errorModal');
    modal.style.display = "block";
    setTimeout(() => {
        modal.classList.add('show');
    }, 10);
}

function closeModal() {
    const modal = document.getElementById('errorModal');
    modal.classList.remove('show');
    setTimeout(() => {
        modal.style.display = "none";
    }, 300); 
}

window.onclick = function (event) {
    const modal = document.getElementById('errorModal');
    if (event.target == modal) {
        closeModal();
    }
}

window.onload = function () {
    if (document.getElementById('errorModal').dataset.hasErrors === "true") {
        showModal();
    }
}
