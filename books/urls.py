from django.contrib import admin
from django.urls import path
from .views import register, my_books, all_books, add_book, profile_view
from django.conf import settings
from django.conf.urls.static import static
 


urlpatterns = [
    path('register/', register, name='register'),
    path('my_books/', my_books, name='my_books'),
    path('all_books/', all_books, name='all_books'),
    path('add_book/', add_book, name='add_book'),
     path('accounts/profile/', profile_view, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)