from ClassBasedViewsBook.models import Book
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework.response import Response

class ShowAllBooks(APIView):
    def get(req):

        books = Book.objects.all()
        serialized_data = BookSerializer(books, many=True)

        return Response(serialized_data.data, status=status.HTTP)