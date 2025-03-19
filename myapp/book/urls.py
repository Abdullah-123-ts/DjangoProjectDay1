from django.urls import path
from book.views import showAllBooks

urlpatterns = [
    path("AddShowBooks/", showAllBooks , name='all_books'),
]
