import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.core.validators import MinValueValidator
from laboratorio.models import Laboratorio
from paciente.models import Paciente

# Create your models here.

class Medicamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'Paciente Asociado')
    nombre = models.CharField(max_length = 60, verbose_name = 'Nombre Medicamento')
    class Presentacion(models.TextChoices):
        CAPSULAS = 'Cápsulas', _('Cápsulas')
        PASTILLAS = 'Pastillas', _('Pastillas')
        GRAGEAS = 'Grageas', _('Grageas')
        JARABE = 'Jarabe', _('Jarabe')
        GOTAS = 'Gotas', _('Gotas')
        SOLUCION = 'Solución', _('Solución')
        UNGUENTO = 'Ungüento', _('Ungüento')
        POMADA = 'Pomada', _('Pomada')
        GEL = 'Gel', _('Gel')
        CREMA = 'Crema', _('Crema')
        VIAL = 'Vial', _('Vial')
        OT = 'Otro', _('Otro Tipo de Presentación')
    presentacion = models.CharField(max_length = 80, choices = Presentacion.choices, default = Presentacion.PASTILLAS, verbose_name = 'Presentación')
    pesoBase = models.CharField(max_length = 4, verbose_name = 'Peso Base')
    class Medida(models.TextChoices):
        mcg = 'mcg', _('Microgramos')
        mg = 'mg', _('Miligramos')
        g = 'g', _('Gramos')
        ml = 'ml', _('Mililitros')
        cc = 'cc', _('Centímetros Cúbicos')
        ot = 'otro', _('Otro peso')
    medida = models.CharField(max_length = 4, choices = Medida.choices, default = Medida.mg, verbose_name = 'Medida')
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.CASCADE, null = True, blank = False, verbose_name = 'Laboratorio')
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name = 'Stock')
    dosis = models.PositiveIntegerField(validators=[MinValueValidator(0)], null = True, blank = False, verbose_name = 'Dosis a Administrar')
    class Frecuencia(models.TextChoices):
        UNA = '1', _('1 hora')
        DOS = '2', _('2 horas')
        TRES = '3', _('3 horas')
        CUATRO = '4', _('4 horas')
        SEIS = '6', _('6 horas')
        OCHO = '8', _('8 horas')
        DOCE = '12', _('12 horas')
        V24 = '24', _('24 horas')
        OT = 'Otro', _('Otra Frecuencia')
    frecuencia = models.CharField(max_length = 4, choices = Frecuencia.choices, default = Frecuencia.DOCE, verbose_name = 'Frecuencia')
    observaciones = models.TextField(max_length = 250, verbose_name = 'Observaciones')
    profesional_salud = models.CharField(max_length = 50, null = True, blank = False, verbose_name = 'Profesional que Prescribe')
    consumoDiario = models.PositiveIntegerField(validators=[MinValueValidator(0)], null = True, blank = False, default = 0, verbose_name = 'Consumo Diario')
    contador = models.PositiveIntegerField(validators=[MinValueValidator(0)], null = True, blank = False, default = 0, verbose_name = 'Contador')
    fechaDosis = models.DateField(verbose_name = "Fecha Dosis", null = True, blank = False, default = datetime.date.today)
    ultimaDosis = models.DateTimeField(verbose_name = "Hora última dosis", null = True, blank = False, default = datetime.datetime.now)
    alerta = models.PositiveIntegerField(validators=[MinValueValidator(0)], null = True, blank = False, verbose_name = 'Alerta', default = 1)
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(max_length = 1, choices = Estado.choices, default = Estado.ACTIVO, verbose_name = 'Estado')
    fechaCreacion = models.DateField(verbose_name = 'Fecha de Creación', null = True, blank = False, default = datetime.date.today)
    



