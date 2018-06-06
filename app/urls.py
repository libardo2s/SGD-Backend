from django.urls import path
from .views import index, PropietarioAPi, getDepartamentos, VehiculoApi, PropietarioUpdateAPi, \
    VehiculoUpdateApi, VinculacionApi

urlpatterns = [
    path('', index, name='index'),
    path('api/propietario/', PropietarioAPi.as_view()),
    path('api/propietario/actualizar/', PropietarioUpdateAPi.as_view()),
    path('api/propietario/eliminar/<int:doc>/', PropietarioUpdateAPi.as_view()),
    path('api/vehiculo/', VehiculoApi.as_view()),
    path('api/vehiculo/actualizar/', VehiculoUpdateApi.as_view()),
    path('api/vehiculo/<int:doc>/', VehiculoApi.as_view()),
    path('api/vehiculo/<str:placa>/', VehiculoUpdateApi.as_view()),
    path('api/vinculacion/', VinculacionApi.as_view()),
    path('departamentos/', getDepartamentos),
]