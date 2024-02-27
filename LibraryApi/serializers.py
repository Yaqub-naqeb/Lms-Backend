from rest_framework import serializers
from .models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

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
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')  # Customize fields as needed
        extra_kwargs = {'password': {'write_only': True}}  # Hide password field

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

