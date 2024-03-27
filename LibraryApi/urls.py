# app/urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, SignupViewSet,LoginAPIView , UserListView , BookingListView,BookingDetailView
from django.urls import include, path

router = DefaultRouter()
router.register(r'books', BookViewSet , basename="books")
router.register('signup', SignupViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users-auth/' ,UserListView.as_view()  , name='users'),
    path('booking/' ,BookingListView.as_view()  , name='booking'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
