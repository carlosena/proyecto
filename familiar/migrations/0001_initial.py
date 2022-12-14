# Generated by Django 4.1.2 on 2022-11-22 23:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nacionalidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro tipo de Documento')], default='C.C', max_length=4, verbose_name='Tipo Documento')),
                ('numDocumento', models.CharField(max_length=50, unique=True, verbose_name='Número Documento')),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('celular', models.CharField(max_length=20, verbose_name='Celular')),
                ('celular2', models.CharField(max_length=20, verbose_name='Celular 2')),
                ('telefono_domicilio', models.CharField(max_length=20, verbose_name='Teléfono Domicilio')),
                ('correo', models.CharField(max_length=60, verbose_name='Correo')),
                ('direccion', models.CharField(max_length=70, verbose_name='Dirección')),
                ('ciudad', models.CharField(max_length=60, null=True, verbose_name='Ciudad o Municipio')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('fechaCreacion', models.DateField(default=datetime.date.today, null=True, verbose_name='Fecha de Creación')),
                ('nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nacionalidad.nacionalidad', verbose_name='Nacionalidad')),
            ],
        ),
    ]
