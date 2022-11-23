import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from familiar.models import Familiar
from eps.models import Eps
from nacionalidad.models import Nacionalidad

# Create your models here.

class Paciente(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        TI = 'T.I', _('Tarjeta de Identidad')
        OT = 'Otro', _('Otro tipo de Documento')
    tipoDocumento = models.CharField(max_length = 4, choices = TipoDocumento.choices, default = TipoDocumento.CC, verbose_name = "Tipo Documento")
    numDocumento = models.CharField(max_length = 50, unique = True, verbose_name = "Número de Documento")
    nombres = models.CharField(max_length = 60, verbose_name = "Nombres")
    apellidos = models.CharField(max_length = 60, verbose_name = "Apellidos")
    fechaNacimiento = models.DateField(verbose_name = "Fecha de Nacimiento", help_text = u"DD/MM/AAAA")
    class Genero(models.TextChoices):
        FEMENINO = 'F', _('Femenino') 
        MASCULINO = 'M', _('Masculino')
        OTRO = 'Otro', _('Otro Género')
    genero = models.CharField(max_length = 4, choices = Genero.choices, default = Genero.FEMENINO, verbose_name = "Género")
    class TipoNovedad(models.TextChoices):
        INGRESO = 'Ingreso', _('Ingreso')
        SALIDA = 'Salida', _('Salida')
    tipoNovedad = models.CharField(max_length = 7, choices = TipoNovedad.choices, default = TipoNovedad.INGRESO, verbose_name = "Tipo Novedad")
    fechaNovedad = models.DateField(verbose_name = "Fecha Novedad", help_text = u"DD/MM/AAAA")
    eps = models.ForeignKey(Eps, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'EPS')
    familiar = models.ForeignKey(Familiar, on_delete = models.CASCADE, null = True, blank = False, verbose_name = "Persona Responsable")
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete = models.CASCADE, null = True, blank = False, verbose_name = "Nacionalidad")
    observaciones = models.TextField(max_length = 250, verbose_name = "Observaciones")
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(max_length = 1, choices = Estado.choices, default = Estado.ACTIVO, verbose_name = "Estado")
    fechaCreacion = models.DateField(verbose_name = 'Fecha de Creación', null = True, blank = False, default = datetime.date.today)
    


    def __str__(self)->str:
        return '%s %s' %(self.nombres, self.apellidos)