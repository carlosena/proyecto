# Generated by Django 4.1.2 on 2022-11-22 23:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('familiar', '0001_initial'),
        ('nacionalidad', '0001_initial'),
        ('eps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro tipo de Documento')], default='C.C', max_length=4, verbose_name='Tipo Documento')),
                ('numDocumento', models.CharField(max_length=50, unique=True, verbose_name='Número de Documento')),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('fechaNacimiento', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Nacimiento')),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('Otro', 'Otro Género')], default='F', max_length=4, verbose_name='Género')),
                ('tipoNovedad', models.CharField(choices=[('Ingreso', 'Ingreso'), ('Salida', 'Salida')], default='Ingreso', max_length=7, verbose_name='Tipo Novedad')),
                ('fechaNovedad', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha Novedad')),
                ('observaciones', models.TextField(max_length=250, verbose_name='Observaciones')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('fechaCreacion', models.DateField(default=datetime.date.today, null=True, verbose_name='Fecha de Creación')),
                ('eps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eps.eps', verbose_name='EPS')),
                ('familiar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='familiar.familiar', verbose_name='Persona Responsable')),
                ('nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nacionalidad.nacionalidad', verbose_name='Nacionalidad')),
            ],
        ),
    ]
