from django.urls import path
from SerializerRelationships.api.views import BooksAuthorAPIView, GenreAPIView, BooksAPIView

urlpatterns = [
    path("hyperLinks/<int:pk>", BooksAuthorAPIView.as_view() , name='all_books'),
    path("hyperLinks/", BooksAuthorAPIView.as_view() , name='all_books'),
    path("genre/", GenreAPIView.as_view() , name='genre'),
    path("books/", BooksAPIView.as_view() , name='books'),
    path("books/<int:pk>", BooksAPIView.as_view() , name='books'),
]
