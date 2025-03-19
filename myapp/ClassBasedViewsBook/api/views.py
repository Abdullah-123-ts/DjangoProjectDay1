from book.models import Book
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from book.serializers import BookSerializer

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