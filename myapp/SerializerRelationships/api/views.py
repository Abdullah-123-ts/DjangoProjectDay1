from rest_framework.generics import ListCreateAPIView
from SerializerRelationships.models import Book2, Author2, Genre
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from SerializerRelationships.serializers import BookSerializer, AuthorSerializer, GenreSerializer

class BooksAuthorAPIView(APIView):

    def get(self, request):
        queryset = Author2.objects.all()
        # serialized_data = AuthorSerializer(queryset, many=True, context={'request': request})
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
        queryset = Book2.objects.all()
        # serialized_data = AuthorSerializer(queryset, many=True, context={'request': request})
        serialized_data = BookSerializer(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GenreAPIView(APIView):

    def get(self, request):
        queryset = Genre.objects.all()
        serialized_data = GenreSerializer(queryset, many=True)
        return Response(serialized_data.data ,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
