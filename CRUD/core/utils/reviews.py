from django.shortcuts import get_object_or_404, redirect
from core.models import Book, Review
from core.forms import ReviewForm

def get_book_review(user, api_id):
    book = get_object_or_404(Book, api_id=api_id)
    if Review.objects.filter(user=user, book=book).exists():
        return book, True
    return book, False

def process_review_form(request, book):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.book_cover = book.cover 
            review.save()
            return redirect('home'), None
    else:
        form = ReviewForm()
    return None, form

def get_review_and_book(user, review_id):
    review = get_object_or_404(Review, id=review_id, user=user)
    return review, review.book

def process_update_form(request, review):
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            print("Formulário válido. Redirecionando para a página de listagem de avaliações...")
            return redirect('read'), None
        else:
            print("Formulário inválido.")
    else:
        form = ReviewForm(instance=review)
    return None, form
