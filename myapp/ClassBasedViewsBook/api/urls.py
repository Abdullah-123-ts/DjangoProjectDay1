from django.urls import path
from ClassBasedViewsBook.api.views import ShowAllBooks, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path("AddShowBooks/", ShowAllBooks.as_view() , name='all_books'),
    path("AddShowBooks/", ShowAllBooks.as_view() , name='all_books'),
    path("AddShowBooks/<int:id>", RetrieveUpdateDestroyAPIView.as_view() , name='get_individual_books'),
]
