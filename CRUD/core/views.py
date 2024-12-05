from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from core.utils.reviews import get_book_review, get_review_and_book, process_review_form, process_update_form
from core.utils.books import paginate_books, process_book, search_books
from core.models import Book, Review
from core.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
def home(request):
    return render(request, 'home.html')

def create (request):
    title = request.GET.get('query', None)
    books = search_books(title)
    
    if not books:
        print("Nenhum livro encontrado.")
        
    page_obj = paginate_books(request, books)
    books_info = [process_book(book) for book in page_obj.object_list]
    
    return render(request, 'catalogue.html', {'page_obj': page_obj, 'books': books_info})

@login_required
def check_review(request, book_id):
    try:
        book = Book.objects.get(api_id=book_id)
        review = Review.objects.filter(book=book, user=request.user).first()

        if review:
            return JsonResponse({'has_review': True, 'review_id': review.id})
        else:
            return JsonResponse({'has_review': False})

    except Book.DoesNotExist:
        return JsonResponse({'has_review': False})


def book_detail(request, id):
    print(f"Procurando livro com id: {id}")
    try:
        book = Book.objects.get(api_id=id)
    except Book.DoesNotExist:
        raise Http404("Livro não encontrado.")

    catalog_url = '/create/'  

    return render(request, 'book_detail.html', {
        'book': book,
        'previous_url': catalog_url,
    })

    
@login_required
def add_review(request, id):
    book, review_exists = get_book_review(request.user, id)
    
    if review_exists:
        return redirect('book_detail', id=book.api_id)
    
    redirect_response, form = process_review_form(request, book)
    
    if redirect_response:
        return redirect_response
    
    return render(request, 'add_review.html', {'form':form, 'book': book})

@login_required
def delete(request):
    reviews = Review.objects.filter(user=request.user).select_related('book')  
    return render(request, 'remove.html', {'reviews': reviews})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('delete') 
    return HttpResponseForbidden()  

@login_required
def read(request):
    reviews = Review.objects.filter(user=request.user).select_related('book')  
    return render(request, 'read.html', {'reviews': reviews})

@login_required
def update(request, review_id):
    review, book = get_review_and_book(request.user, review_id)
    
    redirect_response, form = process_update_form(request, review)
    
    if redirect_response:
        return redirect_response
    
    return render(request, 'update.html', {'form': form, 'book': book})

@user_passes_test(lambda u: not u.is_authenticated, login_url='home')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html' 
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            return redirect('home') 
        return super().dispatch(request, *args, **kwargs)
    
class CustomLogoutView(LogoutView): 
    def dispatch(self, request, *args, **kwargs): 
        print("Logout view reached") 
        return super().dispatch(request, *args, **kwargs)
    
@login_required
def profile(request):
    user = request.user
    reviews = Review.objects.filter(user=user)[:3]  
    
    return render(request, 'profile.html', {
        'user': user,
        'reviews': reviews
    })