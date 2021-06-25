from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
        labels = {
            'name': "Название книги",
            'description': "Описание книги",
            'count': "Количество книг в библиотеке",
            'authors': "Авторы книги"
        }


    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].empty_label = 'Выберите одну или несколько книг'