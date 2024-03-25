from rest_framework import serializers
from .models import Book , Booking
from django.contrib.auth import get_user_model

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

class BooksWithCountSerializer(serializers.Serializer):
    book_count = serializers.IntegerField()
    books = BookSerializer(many=True)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password','first_name' , 'last_name' , 'id')  # Customize fields as needed
        extra_kwargs = {'password': {'write_only': True} , 'id':{'read_only': True}}  # Hide password field

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    
class BookingSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Booking
        fields = ('booking_date', 'book', 'user')

    def create(self, validated_data):
        book_data = validated_data.pop('book')
        user_data = validated_data.pop('user')
        book = Book.objects.create(**book_data)
        user = User.objects.create(**user_data)
        booking = Booking.objects.create(book=book, user=user, **validated_data)
        return booking