from django.shortcuts import render
from. models import Book
# Create your views here.

def book_list(request):
    books = Book.objects.all()

    context = {
        'books_key':books
    }

    return render(request,'catalog/book_list.html', context)