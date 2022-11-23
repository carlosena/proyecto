from django.urls import path
from eps.views import eps, eps_crear, eps_editar, eps_eliminar, eps_listar

urlpatterns = [
    path('', eps, name = 'eps'),
    path('crear/', eps_crear, name = 'eps-crear'),
    path('editar/<int:pk>/', eps_editar, name = 'eps-editar'),
    path('eliminar/<int:pk>/', eps_eliminar,name = 'eps-eliminar'),
    path('listar/', eps_listar, name = 'eps-listar')
]