from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination 
    def list(self, request, *args, **kwargs):
        # Get the queryset of all books
        queryset = self.filter_queryset(self.get_queryset())
        
        # Calculate the count of all books
        book_count = queryset.count()

        # Serialize the data and include the count
        serializer = BookSerializer(queryset, many=True)
        data = {
            'book_count': book_count,
            'books': serializer.data
        }
        return Response(data)
    
    
    
    
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer
    
    # def get_queryset(self):
        
    #     return Book.objects.filter(  )
    
     # You can override the create method to handle "Create" operation
    # def perform_create(self, serializer):
    #     serializer.save()

    # # You can override the update method to handle "Update" operation
    # def perform_update(self, serializer):
    #     serializer.save()

    # You can override the destroy method to handle "Delete" operation
    # def perform_destroy(self, instance):
    #     instance.delete()


# class JustForTest(viewsets.ModelViewSet):
    