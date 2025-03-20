from django.urls import path
from ClassBasedViewsBook.api.views import ShowAllBooks, RetrieveUpdateDestroyAPIView, BooksAuthorAPIView, BooksAPIView

urlpatterns = [
    path("AddShowBooks/", ShowAllBooks.as_view() , name='all_books'),
    path("AddShowBooks/", ShowAllBooks.as_view() , name='all_books'),
    path("AddShowBooks/<int:id>", RetrieveUpdateDestroyAPIView.as_view() , name='get_individual_books'),
    path("AuthorBooks/", BooksAuthorAPIView.as_view() , name='get_author_books'),
    path("Books/", BooksAPIView.as_view() , name='get_author_books'),
]
