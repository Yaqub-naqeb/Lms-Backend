# app/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'genre': ['exact', 'icontains'],  # You can add more filter options here
        }
