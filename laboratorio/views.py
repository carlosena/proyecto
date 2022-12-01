from django.shortcuts import render, redirect 
from laboratorio.forms import LaboratorioForm
from laboratorio.models import Laboratorio
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def laboratorio(request):
    titulo = 'Laboratorio'
    cargaInicial = Laboratorio.objects.all()
    labs = []
    for lab in cargaInicial:
        if lab.estado != '0':
            labs.append(lab)

    context = {
        'titulo': titulo,
        'laboratorios': labs,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/'
    }
    return render(request, 'laboratorio/laboratorio.html', context)


@login_required
def laboratorio_listar(request):
    titulo = 'Laboratorio'
    labs = Laboratorio.objects.all()
    context = {
        'titulo': titulo,
        'laboratorios': labs,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': ''
    }
    return render(request, 'laboratorio/laboratorio-listar.html', context)


@login_required
def laboratorio_crear(request):
    titulo = 'Laboratorio'
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio creado correctamente')
            return redirect('laboratorio')
        else:
            print("Error")
    else:
        form = LaboratorioForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/' 
    }
    return render(request, 'laboratorio/laboratorio-crear.html', context)


@login_required
def laboratorio_editar(request, pk):
    titulo = "Laboratorio"
    lab = Laboratorio.objects.get(id = pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance = lab)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio editado correctamente')
            return redirect('laboratorio')
        else:
            print("Error al guardar")
    else:
        form = LaboratorioForm(instance = lab)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'laboratorio/laboratorio-crear.html', context)


@login_required
def laboratorio_eliminar(request, pk):
    Laboratorio.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('laboratorio')