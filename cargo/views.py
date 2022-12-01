from django.shortcuts import render, redirect 
from cargo.forms import CargoForm 
from cargo.models import Cargo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def cargo(request):
    titulo = 'Cargo'
    cargaInicial = Cargo.objects.all()
    cargos = []
    for cargo in cargaInicial:
        if cargo.estado != '0':
            cargos.append(cargo)
    context = {
        'titulo': titulo,
        'cargos': cargos,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/'
    }
    return render(request, 'cargo/cargos.html', context)


@login_required
def cargo_listar(request):
    titulo = 'Cargo'
    cargos = Cargo.objects.all()
    context = {
        'titulo': titulo,
        'cargos': cargos,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': '' 
    }
    return render(request, 'cargo/cargos-listar.html', context)


@login_required
def cargo_crear(request):
    titulo = 'Cargo'
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo creado correctamente')
            return redirect('cargos')
        else:
            print('Error')
    else: 
        form = CargoForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'cargo/cargos-crear.html', context)


@login_required
def cargo_editar(request, pk):
    titulo = 'Cargo'
    cargo = Cargo.objects.get(id = pk)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance = cargo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo editado correctamente')
            return redirect('cargos')
        else: 
            print('Error al guardar')
    else:
        form = CargoForm(instance = cargo)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'cargo/cargos-crear.html', context)


@login_required
def cargo_eliminar(request, pk):
    Cargo.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('cargos')