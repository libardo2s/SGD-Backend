from rest_framework import serializers

from .serializerPersona import PersonaSerializer
from .models import Taxista


class TaxistaSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=False)

    class Meta:
        model = Taxista
        fields = ('id', 'celular', 'tipo_sangre', 'fecha_vinculacion', 'fecha_nacimiento', 'foto', 'persona')
