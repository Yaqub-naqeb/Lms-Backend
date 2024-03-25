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
        fields = ('first_name' , 'last_name' , 'username','email','password','id','is_staff')  # Customize fields as needed
        extra_kwargs = {'password': {'write_only': True} , 'id':{'read_only': True}}  # Hide password field

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    
    

    
class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    admin = UserSerializer(required=False)
    book = BookSerializer()

    class Meta:
        model = Booking
        fields = ('id', 'booking_date', 'deadline_date', 'user', 'admin', 'book', 'isPending', 'isBooked')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        admin_data = validated_data.pop('admin', None)
        book_data = validated_data.pop('book')

        user = User.objects.create(**user_data)
        admin = User.objects.create(**admin_data) if admin_data else None
        book = Book.objects.create(**book_data)

        booking = Booking.objects.create(user=user, admin=admin, book=book, **validated_data)
        return booking


