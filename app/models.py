import datetime

from django.db import models


# Create your models here.
class Persona(models.Model):
    numero_documento = models.IntegerField(unique=True)
    nombres = models.CharField('Nombres', max_length=80)
    apellidos = models.CharField('Nombres', max_length=80)
    direccion = models.CharField('Nombres', max_length=60)
    departamento = models.CharField('Departamento', max_length=30, null=True)
    municipio = models.CharField('Municipio', max_length=30, null=True)
    telefono = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)


class Propietario(models.Model):
    activo = models.BooleanField(default=True)
    fecha_cumpleanos = models.DateField('Fecha Cumpleaños')
    vial = models.CharField('Vial', max_length=20, unique=True)
    persona = models.OneToOneField(Persona, related_name='persona_propietario', on_delete=models.CASCADE)

    def count_taxis(self):
        return Vehiculo.objects.filter(propietario__id=self.id).count

    taxis = property(count_taxis)

    def __str__(self):
        return '%s %s' % (self.persona.nombres, self.persona.apellidos)


class Vehiculo(models.Model):
    marca = models.CharField('Marca', max_length=10)
    placa = models.CharField('Placa', max_length=6, unique=True)
    color = models.CharField('Color', max_length=10)
    numero_licencia = models.CharField('Número licencia', max_length=10)
    linea = models.CharField('Línea', max_length=10)
    chasis = models.CharField('Chasis', max_length=10, unique=True)
    pasajeros = models.CharField('Pasajeros', max_length=2)
    carroceria = models.CharField('Carroceria', max_length=10)
    modelo = models.CharField('Modelo', max_length=20)
    motor = models.CharField('Motor', max_length=20, unique=True)
    cilindraje = models.CharField('Cilindraje', max_length=20)
    propietario = models.ForeignKey(Propietario, related_name='propietario_vehiculo', on_delete=models.CASCADE)

    def __str__(self):
        return self.placa


class VinculacionVehiculo(models.Model):
    radicado = models.CharField('Radicado', max_length=8, unique=True)
    vehiculo = models.OneToOneField(Vehiculo, related_name='vinculacion_vehiculo', on_delete=models.CASCADE)
    licencia = models.FileField('Licencia', upload_to='vinculacion/licencia', null=True)
    soat = models.FileField('SOAT', upload_to='vinculacion/soat', null=True)
    fecha_vencimiento_soat = models.DateField('Vencimiento SOAT', null=True)
    tecnomecanica = models.FileField('Tecnomecánica', upload_to='vinculacion/tecnomecanica', null=True)
    fecha_vencimiento_tecnomecanica = models.DateField('Vencimiento tecnomecánica', null=True)
    targeta_operacion = models.FileField('Targeta de operación', upload_to='vinculacion/targeta_operacion', null=True)
    fecha_vencimiento_targeta_operacion = models.DateField('Vencimiento targeta de operación', null=True)
    seguro_accidente_personal = models.FileField('Seguro de accidente personal',
                                                 upload_to='vinculacion/seguro_accidente', null=True)
    fecha_vencimiento_seguro_accidente = models.DateField('Vencimiento seguro accidente personal', null=True)
    seguro_extracontractual = models.FileField('Seguro extracontractual', upload_to='vinculacion/seguro_extra', null=True)
    fecha_vencimiento_seguro_extracontractual = models.DateField('Vencimiento seguro extracontractual', null=True)
    seguro_contractual = models.FileField('Seguro contractual', upload_to='vinculacion/seguro_contra', null=True)
    fecha_vencimiento_seguro_contractual = models.DateField('Vencimiento seguro contractual', null=True)
    revision_preoperacional = models.FileField('Seguro preoperacional', upload_to='vinculacion/preoperacional', null=True)
    rut = models.FileField('RUT', upload_to='vinculacion/rut', null=True)
    antecedentes = models.FileField('Antecendentes', upload_to='vinculacion/antecedetes', null=True)
    fecha_vinculacion = models.DateField('Fecha vinculación', default=datetime.date.today)

    def __str__(self):
        return self.vehiculo.placa


class Taxista(models.Model):
    fecha_nacimiento = models.DateField('Fecha_nacimiento')
    foto = models.ImageField('Foto', upload_to='taxista/foto')
    celular = models.CharField('Celular', max_length=10)
    tipo_sangre = models.CharField('Tipo de sangre', max_length=2)
    vinculacion = models.OneToOneField(VinculacionVehiculo, related_name='vinculacion_vehiculo',
                                       on_delete=models.CASCADE, null=True)
    persona = models.OneToOneField(Persona, related_name='persona_taxista', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.persona.nombres, self.persona.apellidos)


class Empleado(models.Model):
    salario = models.IntegerField()
    fecha_inicio_contrato = models.DateField('Fecha incio contrato')
    fecha_finalizacion_contrato = models.DateField('Fecha finalización contrato')
    persona = models.OneToOneField(Persona, related_name='persona_empleado', on_delete=models.CASCADE)
