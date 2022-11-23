from django.shortcuts import render, redirect
from familiar.forms import FamiliarForm
from familiar.models import Familiar
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def familiar(request):
    titulo = 'Familiar'
    cargaInicial = Familiar.objects.all()
    familiares = []
    for familiar in cargaInicial:
        if familiar.estado != '0':
            familiares.append(familiar)
    
    context = {
        'titulo': titulo,
        'familiares': familiares,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/',
        'urlEliminar': 'eliminar/'       
    }
    return render(request, 'familiar/familiar.html', context)
    

@login_required
def familiar_listar(request):
    titulo = 'Familiar'
    familiares = Familiar.objects.all()
    context = {
        'titulo': titulo,
        'familiares': familiares,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': ''
    }
    return render(request, 'familiar/familiar-listar.html', context)


@login_required
def familiar_crear(request):
    titulo = 'Familiar'
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('familiar')
        else:
            print("Error") 
    else: 
        form = FamiliarForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'familiar/familiar-crear.html', context)


@login_required
def familiar_editar(request, pk):
    titulo = 'Familiar'
    familiar = Familiar.objects.get(id = pk)
    if request.method == 'POST':
        form = FamiliarForm(request.POST, instance = familiar)
        if form.is_valid():
            form.save()
            return redirect('familiar')
        else: 
            print("Error al guardar")
    else: 
        form = FamiliarForm(instance = familiar)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'familiar/familiar-crear.html', context)


@login_required
def familiar_eliminar(request, pk):
    Familiar.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('familiar')
