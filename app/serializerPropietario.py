from rest_framework import serializers

from .serializerPersona import PersonaSerializer
from .models import Propietario


class PropietarioSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=False)

    class Meta:
        model = Propietario
        fields = ('id', 'fecha_cumpleanos', 'vial', 'persona', 'taxis')
