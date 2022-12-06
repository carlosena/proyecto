import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from nacionalidad.models import Nacionalidad
from django.core.validators import MinValueValidator

# Create your models here.

class Familiar(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        PT = 'PST', _('Pasaporte')
        TI = 'T.I', _('Tarjeta de Identidad')
        OT = 'Otro', _('Otro tipo de Documento')
    tipoDocumento = models.CharField(max_length = 4, choices = TipoDocumento.choices, default = TipoDocumento.CC, verbose_name = 'Tipo Documento')
    #numDocumento = models.CharField(max_length = 50, unique = True, verbose_name = 'Número Documento')
    numDocumento = models.PositiveIntegerField(validators=[MinValueValidator(0)], unique = True, verbose_name = 'Número de Documento')
    nombres = models.CharField(max_length = 60, verbose_name = 'Nombres')
    apellidos = models.CharField(max_length = 60, verbose_name = 'Apellidos')
    #celular = models.CharField(max_length = 20, verbose_name = 'Celular')
    celular = models.PositiveIntegerField(validators=[MinValueValidator(0)], unique = True, verbose_name = 'Número de Celular')
    #celular2 = models.CharField(max_length = 20, verbose_name = 'Celular 2')
    celular2 = models.PositiveIntegerField(validators=[MinValueValidator(0)], unique = True, verbose_name = 'Número de Celular Adicional')
    #telefono_domicilio = models.CharField(max_length = 20, verbose_name = 'Teléfono Domicilio')
    telefono_domicilio = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name = 'Teléfono domicilio')
    correo = models.CharField(max_length = 60, verbose_name = 'Correo')
    direccion = models.CharField(max_length = 70, verbose_name = 'Dirección')
    ciudad = models.CharField(max_length = 60, null = True, blank = False, verbose_name = 'Ciudad o Municipio')
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'Nacionalidad')
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(max_length = 1, choices = Estado.choices, default = Estado.ACTIVO, verbose_name = 'Estado')
    fechaCreacion = models.DateField(verbose_name = 'Fecha de Creación', null = True, blank = False, default = datetime.date.today)
    

    def __str__(self)->str:
        return '%s %s' %(self.nombres, self.apellidos)