from django.shortcuts import render, redirect
from books_app.books.models import Book
from books_app.books.forms import BookForm


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def show_book_form(request, form, template):
    context = {
        'form': form
    }
    return render(request, template, context)


def create(request):
    if request.method == 'GET':
        return show_book_form(request, BookForm(), 'create.html')

    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    return show_book_form(request, form, 'create.html')


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "GET":
        form = BookForm(instance=book)
        return show_book_form(request, form, 'edit.html')
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return show_book_form(request, form, 'edit.html')


def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')
