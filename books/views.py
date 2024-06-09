from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, BookForm
from .models import Book
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'A user with this email already exists.')
            else:
                try:
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    if user is not None:
                        login(request, user)
                        return redirect('my_books')
                    else:
                        messages.error(request, 'Authentication failed. Please try again.')
                except IntegrityError:
                    form.add_error(None, 'An error occurred during registration. Please try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def my_books(request):
    books = Book.objects.filter(added_by=request.user)
    return render(request, 'my_books.html', {'books': books})

@login_required
def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('my_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def profile_view(request):
    # Logic to retrieve and display user profile information
    return render(request, 'my_books.html')