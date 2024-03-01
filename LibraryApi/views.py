# from django.shortcuts import render,HttpResponse
# from rest_framework.response import Response
# from rest_framework import viewsets
# from .models import Book
# from .serializers import BookSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import BookFilter
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.pagination import PageNumberPagination


# class CustomPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 100



# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = BookFilter
#     authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     pagination_class = CustomPagination 
    
    
#     def list(self, request, *args, **kwargs):
#         # Get the queryset of all books
#         queryset = self.filter_queryset(self.get_queryset())
        
#         # Calculate the count of all books
#         book_count = queryset.count()

#         # Serialize the data and include the count
#         serializer = BookSerializer(queryset, many=True)
#         data = {
#             'book_count': book_count,
#             'books': serializer.data
#         }
#         return Response(data)
    
    
    
    
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
    
    
from rest_framework.authtoken.models import Token
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Book, User
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100
class PaginationSize(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 6  # Default page size

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination 
    
    
    
   
    @action(detail=False)
    def count(self, request):
        book_count = self.get_queryset().count()
        return Response({'book_count': book_count})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Apply pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = BookSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # for image
    
    @action(detail=False, methods=['GET'])
    def custom_action(self, request):
        # Your custom action logic goes here
        data = {"message": "This is a custom action!"}
        return Response(data)


class SignupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to signup
  
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    



class LoginAPIView(APIView):
    permission_classes = []  # Remove all permission classes

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)