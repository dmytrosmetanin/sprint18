from django.shortcuts import render, redirect

from .models import Book
from .book_form import BookForm

from rest_framework import viewsets
from .serializer import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_list(request):
    context = {}
    all_book = Book.get_all()
    context.update({'all_book': all_book})
    return render(request, 'book/all_book.html', context)


def book_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.get_by_id(id)
            form = BookForm(instance=book)

        return render(request, 'book/book_form.html', {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)

        else:
            author = Book.get_by_id(id)
            form = BookForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('book:book_list')


def book_delete(request, id):
    Book.delete_by_id(id)
    return redirect('book:book_list')
