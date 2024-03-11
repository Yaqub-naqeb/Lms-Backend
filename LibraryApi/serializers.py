from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('id', 'title', 'author', 'genre', 'publication_date', 'is_booked', 'cover_image', 'category_name')
        
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

class BooksWithCountSerializer(serializers.Serializer):
    book_count = serializers.IntegerField()
    books = BookSerializer(many=True)
    



