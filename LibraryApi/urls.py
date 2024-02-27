# app/urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, SignupViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register('signup', SignupViewSet, basename='signup')
# router.register('csrf', MyView, basename='csrf')




urlpatterns = [
    path('', include(router.urls)),

]

# urlpatterns = router.urls