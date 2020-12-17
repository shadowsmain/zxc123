from django.shortcuts import render

from bookapp.models import Book


def book(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'page_title': 'книги',
    }

    return render(request, 'bookapp/book.html', context)