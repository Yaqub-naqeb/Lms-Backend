from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from django.urls import include, path
from .views import StudentViewSet, SignUpView, SignInView

router = DefaultRouter()

router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]
