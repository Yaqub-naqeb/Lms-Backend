# app/urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = router.urls
