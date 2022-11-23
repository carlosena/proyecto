from django.shortcuts import render, redirect
from eps.models import Eps
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

@login_required
def usuarios(request):
    titulo = 'Usuarios'
    cargaInicial = Usuario.objects.all()
    usuarios = []
    for usuario in cargaInicial:
        if usuario.estado != '0':
            usuarios.append(usuario)
    
    context = {
        'titulo': titulo,
        'usuarios': usuarios,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/'
    }
    return render(request, 'usuarios/usuarios.html', context)


@login_required
def usuarios_listar(request):
    titulo = 'Usuarios'
    usuarios = Usuario.objects.all()
    context = {
        'titulo': titulo,
        'usuarios': usuarios,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': ''
    }
    return render(request, 'usuarios/usuarios-listar.html', context)


@login_required
def usuarios_crear(request):
    titulo = "Usuarios"
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(request.POST['alias'], request.POST['correo'], 'Sanmartin2022')
            
            user.save()
            
            #messages.success(request, 'Usuario creado correctamente')

            return redirect('usuarios')
            
        else: 

            print('Error')
    else:
        form = UsuarioForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'usuarios/usuarios-crear.html', context)


@login_required
def usuarios_editar(request, pk):
    titulo = "Usuarios"
    usuario = Usuario.objects.get(id = pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else: 
        form = UsuarioForm(instance = usuario)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'usuarios/usuarios-crear.html', context)


@login_required
def usuarios_eliminar(request, pk):   
    Usuario.objects.filter(id = pk).update(
        estado = '0'
    )    
    return redirect('usuarios')



    


