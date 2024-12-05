
    function checkReview(bookId, isAuthenticated) {
        if (!isAuthenticated) {
            window.location.href = `/book/${bookId}/`;
            return;
        }

        fetch(`/check_review/${bookId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.has_review) {
                    document.getElementById('edit-review-btn').href = `/update/${data.review_id}/`;
                    showModal();
                } else {
                    window.location.href = `/book/${bookId}/`;
                }
            });
    }

    function showModal() {
        const modal = document.getElementById('reviewModal');
        modal.style.display = "block";
        setTimeout(() => {
            modal.classList.add('show');
        }, 10);
    }

    function closeModal() {
        const modal = document.getElementById('reviewModal');
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = "none";
        }, 300); 
    }

    window.onclick = function (event) {
        const modal = document.getElementById('reviewModal');
        if (event.target == modal) {
            closeModal();
        }
    }
