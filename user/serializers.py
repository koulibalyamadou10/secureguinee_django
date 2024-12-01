from rest_framework import serializers

from message.models import Message
from user.models import SCUser

class SCUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCUser
        fields = ['id', 'nom', 'prenom', 'numero' ]

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['message']