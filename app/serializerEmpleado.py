from rest_framework import serializers

from .serializerPersona import PersonaSerializer
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=False)

    class Meta:
        model = Empleado
        fields = ('id', 'salario', 'fecha_inicio_contrato', 'fecha_finalizacion_contrato', 'persona')
