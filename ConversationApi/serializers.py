from rest_framework import serializers
from .models import Conversation, Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    sender_username = serializers.StringRelatedField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_username', 'message', 'timestamp']

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    messages = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages']

    def create(self, validated_data):
        participants_data = validated_data.pop('participants', [])
        message_data = validated_data.pop('messages', [])
        conversation = Conversation.objects.create(**validated_data)
        conversation.participants.set(participants_data)
        for message in message_data:
            Message.objects.create(conversation=conversation, **message)
        return conversation

    def update(self, instance, validated_data):
        participants = validated_data.pop('participants', [])
        messages_data = validated_data.pop('messages', [])
        instance = super().update(instance, validated_data)
        instance.participants.set(participants)
        for message_data in messages_data:
            Message.objects.create(conversation=instance, **message_data)
        return instance
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            return Conversation.objects.filter(participants__id=user_id)
        return Conversation.objects.all()
    
    
    # def create(self, validated_data):
    #     participant_data = validated_data.pop('participants')
    #     conversation = Conversation.objects.create(**validated_data)
    #     for participant in participant_data:
    #         conversation.participants.add(participant['id'])
    #     return conversation

    # def update(self, instance, validated_data):
    #     participant_data = validated_data.pop('participants')
    #     instance = super().update(instance, validated_data)
    #     instance.participants.clear()
    #     for participant in participant_data:
    #         instance.participants.add(participant['id'])
    #     return instance