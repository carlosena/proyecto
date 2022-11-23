import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(max_length = 1, choices = Estado.choices, default = Estado.ACTIVO, verbose_name = 'Estado')
    fechaCreacion = models.DateField(verbose_name = 'Fecha de Creación', null = True, blank = False, default = datetime.date.today)
    

    def __str__(self)->str:
        return '%s' %(self.nombre)