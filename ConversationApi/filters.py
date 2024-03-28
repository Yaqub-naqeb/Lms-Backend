import django_filters
from .models import Conversation, Message
from django.contrib.auth import get_user_model
User = get_user_model()

class ConversationFilter(django_filters.FilterSet):
    participants = django_filters.ModelMultipleChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Conversation
        fields = ['participants']

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    message = django_filters.CharFilter(lookup_expr='icontains')
    timestamp = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Message
        fields = ['sender', 'message', 'timestamp']