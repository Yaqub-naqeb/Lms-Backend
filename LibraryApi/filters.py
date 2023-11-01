# filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')  # Case-insensitive exact match

    class Meta:
        model = Book
        fields = ['category']  # Specify the fields you want to filter on
