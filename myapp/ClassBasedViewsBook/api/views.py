from ClassBasedViewsBook.models import Book, Author
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from book.serializers import BookSerializer
from ClassBasedViewsBook.serializers import BookSerializer, AuthorSerializer

class ShowAllBooks(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveUpdateDestroyAPIView(APIView):
    
    def get(self, request, id):
        try:
            queryset = Book.objects.get(id=id)
            serialized_data = BookSerializer(queryset)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error':"Book not found"}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, id):
        try:
            queryset = Book.objects.get(id=id)
            serialized_data = BookSerializer(queryset, data=request.data)
            if(serialized_data.is_valid()):
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error':"Book not found"}, status=status.HTTP_404_NOT_FOUND)
        


    def delete(self, request, id):
        try:
            queryset = Book.objects.get(id=id)
            queryset.delete()
            return Response(status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error':"Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
class BooksAuthorAPIView(APIView):

    def get(self, request):
        queryset = Author.objects.all()
        serialized_data = AuthorSerializer(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BooksAPIView(APIView):

    def get(self, request):
        queryset = Book.objects.all()
        serialized_data = BookSerializer(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
