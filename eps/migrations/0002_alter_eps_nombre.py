# Generated by Django 4.1.2 on 2022-11-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eps',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]
