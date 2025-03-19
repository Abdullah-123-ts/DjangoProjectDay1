from django.urls import path
from ClassBasedViewsBook.api.views import ShowAllBooks

urlpatterns = [
    path("AddShowBooks/", ShowAllBooks.as_view() , name='all_books'),
]
