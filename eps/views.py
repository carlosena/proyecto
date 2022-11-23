from django.shortcuts import render, redirect 
from eps.forms import EpsForm
from eps.models import Eps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def eps(request):
    titulo = "EPS"
    cargaInicial = Eps.objects.all()
    epss = []
    for eps in cargaInicial:
        if eps.estado != '0':
            epss.append(eps)
    context = {
        'titulo': titulo,
        'eps': epss,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/'
    }
    return render(request, 'eps/eps.html', context)


@login_required
def eps_listar(request):
    titulo = 'EPS'
    eps = Eps.objects.all()
    context = {
        'titulo': titulo,
        'eps': eps,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': ''
    }
    return render(request, 'eps/eps-listar.html', context)


@login_required
def eps_crear(request):
    titulo = 'EPS'
    if request.method == 'POST':
        form = EpsForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get()
            
            return redirect('eps')
        else: 
            print("Error")
    else: 
        form = EpsForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'eps/eps-crear.html', context)


@login_required
def eps_editar(request, pk):
    titulo = 'EPS'
    eps = Eps.objects.get(id = pk)
    if request.method == "POST":
        form = EpsForm(request.POST, instance = eps)
        if form.is_valid():
            form.save()
            return redirect('eps')
        else: 
            print("Error al guardar")
    else:
        form = EpsForm(instance = eps)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'eps/eps-crear.html', context)


@login_required
def eps_eliminar(request, pk):
    Eps.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('eps')

    
