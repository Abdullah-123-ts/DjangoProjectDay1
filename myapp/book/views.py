from book.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from book.serializers import BookSerializer

@api_view(['GET', 'POST'])
def showAllBooks(request):

    if request.method == 'GET':
        books = Book.objects.all()
        booksData = BookSerializer(books, many=True)
        return Response(booksData.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


