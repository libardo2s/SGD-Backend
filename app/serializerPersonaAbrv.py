from rest_framework import serializers

from .models import Persona


class PersonaAbrevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'numero_documento', 'nombres', 'apellidos')