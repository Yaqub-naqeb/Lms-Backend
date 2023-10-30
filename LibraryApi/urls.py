from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import include,path

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]