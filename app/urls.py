from django.urls import path
from django.conf.urls.static import static

from sgdtaxi import settings
from .views import index, PropietarioAPi, getDepartamentos, VehiculoApi, PropietarioUpdateAPi, \
    VehiculoUpdateApi, VinculacionApi, VinculacionDocumentosApi

urlpatterns = [
    path('', index, name='index'),
    path('api/propietario/', PropietarioAPi.as_view()),
    path('api/propietario/<int:pk>/', PropietarioAPi.as_view()),
    path('api/propietario/actualizar/', PropietarioUpdateAPi.as_view()),
    path('api/vehiculo/', VehiculoApi.as_view()),
    path('api/vehiculo/actualizar/', VehiculoUpdateApi.as_view()),
    path('api/vehiculo/<int:doc>/', VehiculoApi.as_view()),
    path('api/vehiculo/<str:placa>/', VehiculoUpdateApi.as_view()),
    path('api/vinculacion/', VinculacionApi.as_view()),
    path('api/vinculacion/<int:pk>/', VinculacionApi.as_view()),
    path('api/vinculacion/documento/', VinculacionDocumentosApi.as_view()),
    path('departamentos/', getDepartamentos),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
