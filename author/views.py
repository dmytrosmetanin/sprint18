from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Author
from .author_form import AuthorForm
from .serializer import AuthorSerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.get_all()
    serializer_class = AuthorSerializer


def author_list(request):
    context = {}
    all_book = Author.get_all()
    context.update({'all_author': all_book})
    return render(request, 'author/all_author.html', context)


def author_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.get_by_id(id)
            form = AuthorForm(instance=author)
        return render(request, 'author/author_form.html', {'form': form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)

        else:
            author = Author.get_by_id(id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('author:author_list')


def author_delete(request, id):
    Author.delete_by_id(id)
    return redirect('author:author_list')
