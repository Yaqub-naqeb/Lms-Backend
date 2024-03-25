from rest_framework.authtoken.models import Token
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Book, User , Booking
from .serializers import BookSerializer , BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter,UserFilter
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
    page_size = 10  # Default page size

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination 
    
    
    def get_queryset(self):
        return Book.objects.order_by('-id')

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
    

# class UserListView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
from rest_framework import generics


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_queryset(queryset)
    

class LoginAPIView(APIView):
    permission_classes = []  # Remove all permission classes

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        is_staff= request.data.get("is_staff")
        user = authenticate(username=username, password=password , is_staff= is_staff)

        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "id": user.id,
                "username": user.username,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "is_staff" : user.is_staff
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class BookingListView(APIView):        
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        booking_date = request.data.get("booking_date")
        deadline_date = request.data.get("deadline_date")
        book_data = request.data.get("book")
        user_data = request.data.get("user")
        admin_data = request.data.get("admin")  # Optional field, can be None
        is_pending = request.data.get("isPending", False)
        is_booked = request.data.get("isBooked", False)

        try:
            book = Book.objects.get(id=book_data['id'])
            user = User.objects.get(id=user_data['id'])
            admin = User.objects.get(id=admin_data['id']) if admin_data else None

            booking = Booking.objects.create(
                booking_date=booking_date,
                deadline_date=deadline_date,
                book=book,
                user=user,
                admin=admin,
                isPending=is_pending,
                isBooked=is_booked
            )

            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

    def delete(self, request, booking_id):
        try:
            booking = Booking.objects.get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking does not exist'}, status=status.HTTP_404_NOT_FOUND)

        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)