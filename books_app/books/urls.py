from django.urls import path

from books_app.books.views import index
from books_app.books.views import create
from books_app.books.views import edit
from books_app.books.views import delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create book'),
    path('edit/<int:pk>', edit, name='edit book'),
    path('delete/<int:pk>', delete, name='delete book'),
]