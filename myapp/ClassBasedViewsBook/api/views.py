from book.models import Book
from rest_framework.generics import ListCreateAPIView
from book.serializers import BookSerializer

class ShowAllBooks(ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
