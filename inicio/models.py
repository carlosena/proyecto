from django.db import models

# Create your models here.

class FechaDeDosis(models.Model):
    fechaDeDosis = models.DateField(verbose_name = "Fecha para dosis", null = True, blank = False, help_text = u"AAAA/MM/DD")
    