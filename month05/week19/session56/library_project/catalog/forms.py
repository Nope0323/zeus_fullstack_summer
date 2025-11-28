from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'published_date', 'isbn']

        labels ={
            'title': 'Номын Нэр', 
            'author_name': 'Зохиогчийн нэр',
            'published_date':'хэвлсэн огноо(YYYY-MM-DD)',
            'isbn': 'isbn дугаар',
        }