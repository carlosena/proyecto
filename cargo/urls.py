from django.urls import path
from cargo.views import cargo, cargo_crear, cargo_editar, cargo_eliminar, cargo_listar

urlpatterns = [ 
    path('', cargo, name = 'cargos'),
    path('crear/', cargo_crear, name = 'cargos-crear'),
    path('editar/<int:pk>/', cargo_editar, name = 'cargos-editar'),
    path('eliminar/<int:pk>/', cargo_eliminar, name = 'cargos-eliminar'),
    path('listar/', cargo_listar, name = 'cargos-listar')
]