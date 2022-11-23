import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from eps.models import Eps
from nacionalidad.models import Nacionalidad
from cargo.models import Cargo
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'C.C', _('Cédula de Ciudadanía')
        CE = 'C.E', _('Cédula de Extranjería')
        TI = 'T.I', _('Tarjeta de Identidad')
        OT = 'Otro', _('Otro tipo de Documento')
    tipoDocumento = models.CharField(max_length = 4, choices = TipoDocumento.choices, default = TipoDocumento.CC, verbose_name = "Tipo de Documento")
    numDocumento = models.CharField(max_length = 50, unique = True, verbose_name = "Número de Documento")
    nombres = models.CharField(max_length = 60, verbose_name = "Nombres")
    apellidos = models.CharField(max_length = 60, verbose_name = "Apellidos")
    foto = models.ImageField(upload_to = 'images/', blank = True, default = 'images/default.png')
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento", help_text = u"DD/MM/AAAA")
    correo = models.CharField(max_length = 60, unique = True, verbose_name = "Correo")
    eps = models.ForeignKey(Eps, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'EPS')
    celular = models.CharField(max_length = 20, verbose_name = "Celular")
    telefono_familiar = models.CharField(max_length = 20, verbose_name = "Teléfono familiar")
    direccion = models.CharField(max_length = 70, verbose_name = "Dirección")
    ciudad = models.CharField(max_length = 60, null = True, blank = False, verbose_name = 'Ciudad o Municipio')
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'Cargo')
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'Nacionalidad')
    class Perfil(models.TextChoices):
        ADMIN = 'admin', _('Administrador')
        USER = 'usuario', _('Usuario')
    perfil = models.CharField(max_length = 7, choices = Perfil.choices, default = Perfil.USER, null = True, blank = False, verbose_name = 'Perfil')
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(max_length = 1, choices = Estado.choices, default = Estado.ACTIVO, verbose_name = "Estado")
    alias = models.CharField(max_length = 15, unique = True, null = True, blank = False, verbose_name = 'Alias usuario')
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = False)
    fechaCreacion = models.DateField(verbose_name = 'Fecha de Creación', null = True, blank = False, default = datetime.date.today)
    

    def __str__(self)->str:
        return '%s %s' %(self.nombres, self.apellidos) 

   

