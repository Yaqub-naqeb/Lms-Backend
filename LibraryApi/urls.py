# app/urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, SignupViewSet,LoginAPIView
from django.urls import include, path

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register('signup', SignupViewSet, basename='signup')
# router.register('loginn', LoginView, basename='login')
# router.register('csrf', MyView, basename='csrf')




urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),


]

# urlpatterns = router.urls