from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
# Create your views here.

def book_list(request):
    books = Book.objects.all()

    context = {
        'books_key':books
    }

    return render(request,'catalog/book_list.html', context)

def create_book(request):
    form = BookForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            form = BookForm()
    return render (request,'catalog/book_form.html',{'form':form})
