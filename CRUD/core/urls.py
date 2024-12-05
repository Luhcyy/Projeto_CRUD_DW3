from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('check_review/<str:book_id>/', views.check_review, name='check_review'),
    path('delete/', views.delete, name='delete'),
    path('delete/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('read/', views.read, name='read'),
    path('update/<int:review_id>/', views.update, name='update'),
    path('book/<str:id>/', views.book_detail, name='book_detail'),
    path('book/<str:id>/add_review', views.add_review, name='add_review'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
