# Generated by Django 4.1.2 on 2022-12-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('PST', 'Pasaporte'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro tipo de Documento')], default='C.C', max_length=4, verbose_name='Tipo de Documento'),
        ),
    ]
