import datetime
from sqlite3 import Date
from django.shortcuts import render, redirect 
from nacionalidad.forms import NacionalidadForm
from nacionalidad.models import Nacionalidad 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def nacionalidad(request):
    titulo = 'Nacionalidad'
    cargaInicial = Nacionalidad.objects.all()
    nacionalidades = []
    for nacionalidad in cargaInicial:
        if nacionalidad.estado != '0':
            nacionalidades.append(nacionalidad)
    context = {
        'titulo': titulo,
        'nacionalidades': nacionalidades,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/'
    }
    return render(request, 'nacionalidad/nacionalidades.html', context)


@login_required
def nacionalidad_listar(request):
    titulo = 'Nacionalidad'
    nacionalidades = Nacionalidad.objects.all()
    context = {
        'titulo': titulo, 
        'nacionalidades': nacionalidades,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': ''
    }
    return render(request, 'nacionalidad/nacionalidades-listar.html', context)


@login_required
def nacionalidad_crear(request):
    titulo = 'Nacionalidad'
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nacionalidades')
        else: 
            print('Error')
    else: 
        form = NacionalidadForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'nacionalidad/nacionalidades-crear.html', context)


@login_required
def nacionalidad_editar(request, pk):
    titulo = 'Nacionalidad'
    nacionalidad = Nacionalidad.objects.get(id = pk)
    if request.method == 'POST':
        form = NacionalidadForm(request.POST, instance = nacionalidad)
        if form.is_valid():
            form.save()
            return redirect('nacionalidades')
        else:
            print('Error al guardar')
    else: 
        form = NacionalidadForm(instance = nacionalidad)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'nacionalidad/nacionalidades-crear.html', context)


@login_required
def nacionalidad_eliminar(request, pk):
    Nacionalidad.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('nacionalidades')


def contadorCero():
    fecha = datetime.now()
    print(fecha)