from django.urls import path
from paciente.views import pacientes, pacientes_crear, pacientes_editar, pacientes_eliminar, pacientes_listar

urlpatterns = [ 
    path('', pacientes, name = 'pacientes'),
    path('listar/', pacientes_listar, name = 'pacientes-listar'),
    path('crear/', pacientes_crear, name = 'pacientes-crear'),
    path('editar/<int:pk>/', pacientes_editar, name = 'pacientes-editar'),
    path('eliminar/<int:pk>/', pacientes_eliminar, name = 'pacientes-eliminar')
]