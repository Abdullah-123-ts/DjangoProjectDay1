from rest_framework import serializers
from SerializerRelationships.models import Book2, Author2, Genre
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    # title = serializers.PrimaryKeyRelatedField(queryset=Author2.objects.all())
    # title = serializers.StringRelatedField(many=True)
    published_since = serializers.SerializerMethodField()

    class Meta:
        model = Book2
        fields = "__all__"

    def get_published_since(self, obj):
        time = date.today()
        return(time-obj.Published_date).days


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author2
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book2.objects.all()) 
    # book = serializers.StringRelatedField(many=True)

    # book = BookSerializer(many=True) 
    class Meta:
        model = Genre
        fields = "__all__"