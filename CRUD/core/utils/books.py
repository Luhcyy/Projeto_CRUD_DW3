from django.core.paginator import Paginator
from django.utils.text import slugify
from tempfile import NamedTemporaryFile
from django.core.files import File
import requests
from core.models import Book
from core.services.api import GoogleBooksAPI

def search_books(title=None):
    if title:
        return GoogleBooksAPI.search_books_by_title(title)
    return GoogleBooksAPI.search_books_by_title('bestsellers')

def paginate_books(request, books, per_page=9):
    paginator = Paginator(books, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

def process_book(book_data):
    api_id = book_data.get('id')
    book_obj = Book.objects.filter(api_id=api_id).first()
    
    if not book_obj:
        volume_info = book_data.get('volumeInfo', {})
        title = volume_info.get('title', 'Título não disponível')
        author = ', '.join(volume_info.get('authors', ['Desconhecido']))
        cover_url = volume_info.get('imageLinks', {}).get('thumbnail', None)
        synopsis = volume_info.get('description', 'Sinopse não disponível.')
        slug = slugify(title)
        
        while Book.objects.filter(slug=slug).exists():
            slug = f"{slug}-{api_id}"

        book_obj = Book(
            api_id=api_id,
            title=title,
            author=author,
            synopsis=synopsis,
            slug=slug,
        )

        if cover_url:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(requests.get(cover_url).content)
            img_temp.flush()
            book_obj.cover.save(f"{slug}.jpg", File(img_temp))

        book_obj.save()
    
    return {
        'title': book_obj.title,
        'author': book_obj.author,
        'cover': book_obj.cover.url if book_obj.cover else '',
        'api_id': book_obj.api_id,
        'synopsis': book_obj.synopsis
    }
