from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'message', 'sent_at', 'is_read', 'is_sent_by_user', 'image']
