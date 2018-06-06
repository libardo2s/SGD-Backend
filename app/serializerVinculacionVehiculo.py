from rest_framework import serializers

from .serializerVehiculo import VehiculoSerializer
from .models import VinculacionVehiculo


class VinculacionSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer(many=False)

    class Meta:
        model = VinculacionVehiculo
        fields = ('id', 'radicado', 'vehiculo', 'licencia', 'soat', 'fecha_vencimiento_soat',
                  'tecnomecanica', 'fecha_vencimiento_tecnomecanica', 'targeta_operacion',
                  'fecha_vencimiento_targeta_operacion', 'seguro_accidente_personal',
                  'fecha_vencimiento_seguro_accidente', 'seguro_extracontractual',
                  'fecha_vencimiento_seguro_extracontractual', 'seguro_contractual',
                  'fecha_vencimiento_seguro_contractual', 'revision_preoperacional', 'rut', 'antecedentes', 'fecha_vinculacion')
