# filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(lookup_expr='iexact')
    author = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['title','genre' , 'author' , 'publication_date' , 'is_booked' ]  # Specify the fields you want to filter on
