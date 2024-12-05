from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Book, Review, User

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'api_id', 'slug','synopsis')  
    search_fields = ('title', 'author')  
    
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User  
    list_display = ('email', 'full_name', 'is_staff', 'is_active')  
    search_fields = ('email', 'full_name')  
    ordering = ('email',)  
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name',)}),  
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name',)}),  
    )  

admin.site.register(Review)