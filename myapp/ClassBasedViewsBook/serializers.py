from rest_framework import serializers
from ClassBasedViewsBook.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    author = BookSerializer(many=True) 
    class Meta:
        model = Author
        fields = "__all__"

