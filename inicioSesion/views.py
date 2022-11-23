from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def inicioSesion(request):
    titulo = 'Inicio Sesión'
    if request.method == 'GET':
        #return render(request, 'inicioSesion/inicioSesion.html', {
        return render(request, 'registration/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            messages.error(request, 'Contraseñas o Usuario no coinciden')
            return render(request, 'registration/login.html', {
                'titulo': titulo,
                'form': AuthenticationForm, 
                'error': 'Usuario o password incorrectos'
            })
        else: 
            login(request, user)
            return redirect('familiar')


def logedIn(request):
    titulo = 'Inicio Sesión'
    if request.method == 'GET':
        #return render(request, 'inicioSesion/inicioSesion.html', {
        return render(request, 'registration/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            messages.error(request, 'Contraseñas o Usuario no coinciden')
            print("error de autenticación")
            return render(request, 'registration/login.html', {
                'titulo': titulo,
                'form': AuthenticationForm, 
                'error': 'Usuario o password incorrectos'
            })
        else: 
            login(request, user)
            return redirect('familiar')
            




@login_required
def crearSesion(request):
    if request.method == 'GET':
        return render(request, 'inicioSesion/crearSesion.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                print('Registrando Usuario')
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('familiar')
            except IntegrityError:
                messages.error(request, 'Usuario ya existe')
                return render(request, 'inicioSesion/crearSesion.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya Existe'
                })
        messages.error(request, 'Contraseñas no coinciden')
        return render(request, 'inicioSesion/crearSesion.html', {
            'form': UserCreationForm, 
            'error': 'Contraseñas no coinciden'
        })


@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')
