from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
        labels = {
            'name': "Title",
            'description': "Description",
            'count': "Quantity of books at the library",
            'authors': "Authors"
        }


    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].empty_label = 'Choose the book'