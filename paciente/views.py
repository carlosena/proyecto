from django.shortcuts import render, redirect 
from paciente.forms import PacienteForm
from paciente.models import Paciente
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def pacientes(request):
    titulo = 'Pacientes'
    cargaInicial = Paciente.objects.all()
    pacientes = []
    for paciente in cargaInicial:
        if paciente.estado != '0':
            pacientes.append(paciente) 
    context = {
        'titulo': titulo,
        'pacientes': pacientes,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/'
    }
    return render(request, 'pacientes/pacientes.html', context)


@login_required
def pacientes_listar(request):
    titulo = 'Pacientes'
    pacientes = Paciente.objects.all()
    context = {
        'titulo': titulo,
        'pacientes': pacientes,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': ''
    }
    return render(request, 'pacientes/pacientes-listar.html', context) 


@login_required
def pacientes_crear(request):
    titulo = 'Pacientes'
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente creado correctamente')
            return redirect('pacientes')
        else:
            print("Error")
    else:
        form = PacienteForm()
    context = {
        'titulo': titulo,
        'form': form, 
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'pacientes/pacientes-crear.html', context) 


@login_required
def pacientes_editar(request, pk):
    titulo = 'Pacientes'
    paciente = Paciente.objects.get(id = pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance = paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente editado correctamente')
            return redirect('pacientes')
        else:
            print("Error al guardar")
    else: 
        form = PacienteForm(instance = paciente)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    } 
    return render(request, 'pacientes/pacientes-crear.html', context)


@login_required
def pacientes_eliminar(request, pk):
    Paciente.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('pacientes')
