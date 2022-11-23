from django.urls import path
from base.views import inicio
from inicioSesion.views import inicioSesion, crearSesion, cerrarSesion
from usuarios.views import usuarios
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', inicioSesion, name = 'inicioSesion'),
    path('../', inicio, name = 'inicio'),
    path('../', usuarios, name = 'usuarios'),
    path('crearSesion/', crearSesion, name = 'crearSesion'),
    path('cerrarSesion/', cerrarSesion, name = 'cerrarSesion')
]