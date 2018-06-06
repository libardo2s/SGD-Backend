from rest_framework import serializers

from .serializerPersonaAbrv import PersonaAbrevSerializer
from .models import Propietario


class PropietarioAbrevSerializer(serializers.ModelSerializer):
    persona = PersonaAbrevSerializer(many=False)

    class Meta:
        model = Propietario
        fields = ('id', 'persona')
