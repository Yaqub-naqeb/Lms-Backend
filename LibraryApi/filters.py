# filters.py
import django_filters
from .models import Book
from django.contrib.auth import get_user_model
User = get_user_model()

class BookFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(lookup_expr='iexact')
    author = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['title','genre' , 'author' , 'publication_date' , 'is_booked' , 'added_by' , 'updated_by' ,'dewey_decimal_number' , 'dewey_decimal_category_range'   ,'book_code' , 'page_number' ,'publisher' , 'published_place' ]  # Specify the fields you want to filter on

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='iexact')
    first_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User
        fields = [ 'username','is_staff','first_name','last_name','id' ]  # Specify the fields you want to filter on

