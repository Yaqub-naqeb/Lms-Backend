from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination 
    
    
    
    
    
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
    