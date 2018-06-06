# -*- coding: utf-8 -*-
import os
import jwt
import uuid

# DJANGO
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# RESTFRAMEWORK
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# MODELS
from .models import Propietario, Persona, Vehiculo, VinculacionVehiculo

# SERIALIZERS
from .serializerPropietario import PropietarioSerializer
from .serializerVehiculo import VehiculoSerializer
from .serializerVinculacionVehiculo import VinculacionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


class LoginApi(APIView):
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):

        usr = request.data.get('usuario')
        psw = request.data.get('contrasena')

        user = authenticate(username=usr, password=psw)

        if user is not None:
            # payload = jwt_payload_handler(user)
            # token = jwt_encode_handler(payload)
            data = [user.username]

            # serializer_user = UserSerializer(list_user, many=True)
            response = {
                'content': data,
                'isOk': True,
                'message': '',
            }
        else:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Error al intenta ingresar, por favor verifique sus datos e intente nuevamente'
            }
        return Response(response, status=status.HTTP_200_OK)


class PropietarioAPi(APIView):

    def get(self, request, format=None):
        # token = getDataToken(request.META.get('HTTP_AUTHORIZATION'))
        # print(header)
        lista_propietarios = Propietario.objects.filter(activo=True)
        serializer_lista = PropietarioSerializer(lista_propietarios, many=True)
        response = {
            'content': serializer_lista.data,
            'isOk': True,
            'message': ''
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        documento = request.data.get('documento')
        nombres = request.data.get('nombres')
        apellidos = request.data.get('apellidos')
        direccion = request.data.get('direccion')
        departamento = request.data.get('departamento')
        municipio = request.data.get('municipio')
        telefono = request.data.get('telefono')
        fecha = request.data.get('fechanacimiento')
        vial = request.data.get('vial')

        try:
            prop = Propietario.objects.filter(persona__numero_documento=documento)
            if len(prop) == 0:
                vialprop = Propietario.objects.filter(vial=vial)
                if len(vialprop) == 0:
                    propietario = Propietario()
                    persona = Persona()
                    persona.numero_documento = documento
                    persona.nombres = nombres
                    persona.apellidos = apellidos
                    persona.direccion = direccion
                    persona.departamento = departamento
                    persona.municipio = municipio
                    persona.telefono = telefono
                    persona.save()
                    propietario.persona = persona
                    propietario.fecha_cumpleanos = fecha
                    propietario.vial = vial
                    propietario.save()
                    list = [propietario]
                    propietario_seriealizer = PropietarioSerializer(list, many=True)
                    response = {
                        'content': propietario_seriealizer.data,
                        'isOk': True,
                        'message': 'Propietario almacenado exitosamente'
                    }
                else:
                    response = {
                        'content': [],
                        'isOk': True,
                        'message': 'El código vial ya se encuentra registrado'
                    }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': 'El propietario ya se encuentra registrado'
                }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            propietario_list = Propietario.objects.filter(persona__numero_documento=pk)
            propietario = propietario_list[0]
            propietario.activo = False
            propietario.save()
            response = {
                'content': [],
                'isOk': True,
                'message': 'Propietario eliminado correctamente'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Propietario.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Propietario no encontrado'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


class PropietarioUpdateAPi(APIView):

    def get(self, request, doc=None, format=None):
        if doc is not None:
            try:
                propietario_list = Propietario.objects.filter(persona__numero_documento=doc)
                propietario = propietario_list[0]
                propietario.activo = False
                propietario.save()
                response = {
                    'content': [],
                    'isOk': True,
                    'message': 'Propietario eliminado correctamente'
                }
                return Response(response, status=status.HTTP_200_OK)
            except Exception as e:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': 'Propietario no encontrado'
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Propietario no encontrado'
            }
            return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        documento = request.data.get('documento_select')
        nombres = request.data.get('nombres_select')
        apellidos = request.data.get('apellidos_select')
        direccion = request.data.get('direccion_select')
        departamento = request.data.get('departamento_select')
        municipio = request.data.get('municipio_select')
        telefono = request.data.get('telefono_select')
        fecha = request.data.get('fecha_cumpleanos_select')
        vial = request.data.get('vial_select')

        try:
            propietario_list = Propietario.objects.filter(persona__numero_documento=documento)
            persona_list = Persona.objects.filter(numero_documento=documento)
            if len(propietario_list) > 0:
                persona = persona_list[0]
                propietario = propietario_list[0]
                persona.numero_documento = documento
                persona.nombres = nombres
                persona.apellidos = apellidos
                persona.direccion = direccion
                persona.departamento = departamento
                persona.municipio = municipio
                persona.telefono = telefono
                propietario.persona = persona
                propietario.fecha_cumpleanos = fecha
                propietario.vial = vial
                propietario.save()
                list = []
                list.append(propietario)
                propietario_seriealizer = PropietarioSerializer(list, many=True)
                response = {
                    'content': propietario_seriealizer.data,
                    'isOk': True,
                    'message': 'Datos actualizados correctamente'
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'content': [],
                    'isOk': True,
                    'message': 'El documento %s, no se encuentra registrado en el sistema'
                }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


class VehiculoApi(APIView):
    def get(self, request, doc=None, formar=None):
        if doc is not None:
            lista_vehiculos = Vehiculo.objects.filter(propietario__persona__numero_documento=doc)
            serializer_vehiculo = VehiculoSerializer(lista_vehiculos, many=True)
            response = {
                'content': serializer_vehiculo.data,
                'isOk': True,
                'message': ''
            }
        else:
            lista_vehiculos = Vehiculo.objects.all()
            serializer_vehiculo = VehiculoSerializer(lista_vehiculos, many=True)
            response = {
                'content': serializer_vehiculo.data,
                'isOk': True,
                'message': ''
            }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        prop = request.data.get('propietario')
        d_placa = request.data.get('placa')
        d_chasis = request.data.get('chasis')
        d_carroceria = request.data.get('carroceria')
        d_cilindraje = request.data.get('cilindraje')
        d_color = request.data.get('color')
        d_licencia = request.data.get('licencia')
        d_linea = request.data.get('linea')
        d_marca = request.data.get('marca')
        d_modelo = request.data.get('modelo')
        d_motor = request.data.get('motor')
        d_pasajeros = request.data.get('pasajeros')

        try:
            propietario = Propietario.objects.get(persona__numero_documento=prop)
            v_placa = Vehiculo.objects.filter(placa=d_placa)
            if len(v_placa) == 0:
                v_chasis = Vehiculo.objects.filter(chasis=d_chasis)
                if len(v_chasis) == 0:
                    v_motor = Vehiculo.objects.filter(chasis=d_motor)
                    if len(v_motor) == 0:
                        vehiculo = Vehiculo()
                        vehiculo.propietario = propietario
                        vehiculo.placa = d_placa
                        vehiculo.carroceria = d_carroceria
                        vehiculo.chasis = d_chasis
                        vehiculo.cilindraje = d_cilindraje
                        vehiculo.color = d_color
                        vehiculo.linea = d_linea
                        vehiculo.marca = d_marca
                        vehiculo.modelo = d_modelo
                        vehiculo.motor = d_motor
                        vehiculo.numero_licencia = d_licencia
                        vehiculo.pasajeros = d_pasajeros
                        vehiculo.save()
                        response = {
                            'content': [],
                            'isOk': True,
                            'message': 'Vehículo registrado correctamente'
                        }
                    else:
                        response = {
                            'content': [],
                            'isOk': False,
                            'message': 'El motor %s, ya se encuentra registrado en el sistema' % d_motor
                        }
                else:
                    response = {
                        'content': [],
                        'isOk': False,
                        'message': 'El chasis %s, ya se encuentra registrado en el sistema' % d_chasis
                    }
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': 'La placa %s, ya se encuentra registrada en el sistema' % d_placa
                }
            return Response(response, status=status.HTTP_200_OK)
        except Propietario.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Propietario no encontrado'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


class VehiculoUpdateApi(APIView):

    def get(self, request, placa=None, format=None):
        if placa is not None:
            lista_vehiculos = Vehiculo.objects.filter(placa=placa.lower())
            serializer_vehiculo = VehiculoSerializer(lista_vehiculos, many=True)
            response = {
                'content': serializer_vehiculo.data,
                'isOk': True,
                'message': ''
            }
            return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        propietario_doc = request.data.get('propietario')
        vehiculo_id = request.data.get('id')
        vehiculo_modelo = request.data.get('modelo')
        vehiculo_chasis = request.data.get('chasis')
        vehiculo_motor = request.data.get('motor')
        vehiculo_carroceria = request.data.get('carroceria')
        vehiculo_pasajeros = request.data.get('pasajeros')
        vehiculo_color = request.data.get('color')
        vehiculo_licencia = request.data.get('numero_licencia')
        vehiculo_cilindraje = request.data.get('cilindraje')
        vehiculo_marca = request.data.get('marca')
        vehiculo_placa = request.data.get('placa')
        vehiculo_linea = request.data.get('linea')
        try:
            propietario = Propietario.objects.get(persona__numero_documento=propietario_doc)
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)

            vehiculo.propietario = propietario
            vehiculo.modelo = vehiculo_modelo
            vehiculo.chasis = vehiculo_chasis
            vehiculo.motor = vehiculo_motor
            vehiculo.carroceriai = vehiculo_carroceria
            vehiculo.pasajeros = vehiculo_pasajeros
            vehiculo.color = vehiculo_color
            vehiculo.numero_licencia = vehiculo_licencia
            vehiculo.cilindraje = vehiculo_cilindraje
            vehiculo.marca = vehiculo_marca
            vehiculo.placa = vehiculo_placa
            vehiculo.linea = vehiculo_linea
            vehiculo.save()

            lista_vehiulo = [vehiculo]
            serilizer = VehiculoSerializer(lista_vehiulo, many=True)
            response = {
                'content': serilizer.data,
                'isOk': True,
                'message': 'Datos actualizados corretamente'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Vehiculo.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Vehículo no encontrado'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Propietario.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Propietario no encontrado'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


class VinculacionApi(APIView):
    def get(self, request, format=None):
        lista_vinculaciones = VinculacionVehiculo.objects.filter(activo=True)
        serializer_vinculacion = VinculacionSerializer(lista_vinculaciones, many=True)
        response = {
            'content': serializer_vinculacion.data,
            'isOk': True,
            'message': ''
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print(request.data)
        try:
            vehiculo_id = request.data.get('id_vehiculo')
            radicado = random_string()

            vinculacion = VinculacionVehiculo.objects.filter(vehiculo__id=vehiculo_id)
            if len(vinculacion) == 0:
                vehiculo = Vehiculo.objects.get(id=vehiculo_id)
                vinculacion = VinculacionVehiculo.objects.create(radicado=radicado, vehiculo=vehiculo)
                list = [vinculacion]
                serializer_vinculacion = VinculacionSerializer(list, many=True)
                response = {
                    'content': serializer_vinculacion.data,
                    'isOk': True,
                    'message': 'Vehículo vinculado correctamente'
                }
                return Response(response, status=status.HTTP_200_OK)
            elif not vinculacion[0].activo:
                vinculacion[0].activo = True
                vinculacion[0].save()
                serializer_vinculacion = VinculacionSerializer(vinculacion, many=True)
                response = {
                    'content': serializer_vinculacion.data,
                    'isOk': True,
                    'message': 'Vinculación activa'
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': 'Vehículo no encontrado'
                }
                return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'content': str(e),
                'isOk': False,
                'message': ''
            }
            return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            vinculacion = VinculacionVehiculo.objects.get(id=pk)
            vinculacion.activo = False
            vinculacion.save()
            response = {
                'content': [],
                'isOk': True,
                'message': 'Eliminado correctamente'
            }
            return Response(response, status=status.HTTP_200_OK)
        except VinculacionVehiculo.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Elemento no encontrado'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


def getDepartamentos(request):
    f = os.path.join(os.path.dirname(__file__), 'departamentos/colombia.json')
    json_data = open(f)
    return HttpResponse(json_data)


def getDataToken(header):
    split_token = header.split(' ')
    payload = jwt.decode(split_token[1], settings.SECRET_KEY)
    return payload


def random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.
