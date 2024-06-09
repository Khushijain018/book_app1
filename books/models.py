from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    publication_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    genre = models.CharField(max_length=100, default='None')
    pdf = models.FileField(upload_to='book_pdfs/', blank=True, null=True)
    pages = models.PositiveIntegerField(default=0)  # Set default number of pages as 0

    def __str__(self):
        return self.title
