from rest_framework import serializers

from .serializerPropietarioAbrv import PropietarioAbrevSerializer
from .models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    propietario = PropietarioAbrevSerializer(many=False)

    class Meta:
        model = Vehiculo
        fields = ('id', 'marca', 'placa', 'color', 'numero_licencia', 'linea', 'chasis', 'pasajeros', 'carroceria',
                  'modelo', 'motor', 'cilindraje', 'propietario')
