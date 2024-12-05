from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='books/covers/', blank=True, null=True)  
    api_id = models.CharField(max_length=255, unique=True, blank=True, default='default_value')
    slug = models.SlugField(unique=True)  

    def __str__(self):
        return self.title

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  
    completed = models.BooleanField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Review de {self.user.username} para {self.book.title}"
    
