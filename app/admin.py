from django.contrib import admin

# Register your models here.
from .models import Propietario, Vehiculo, Taxista, Empleado, VinculacionVehiculo

admin.site.register(Propietario)
admin.site.register(Vehiculo)
admin.site.register(Taxista)
admin.site.register(Empleado)
admin.site.register(VinculacionVehiculo)