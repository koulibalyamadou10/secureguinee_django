from rest_framework import serializers

from autorite.models import Autorite

class AutoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autorite
        fields = ['id', 'email']
