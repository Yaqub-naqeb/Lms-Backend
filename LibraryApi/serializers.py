from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BooksWithCountSerializer(serializers.Serializer):
    book_count = serializers.IntegerField()
    books = BookSerializer(many=True)
