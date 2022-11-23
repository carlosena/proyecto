from django.urls import path
from medicamento.views import medicamento, medicamento_crear, medicamento_editar, medicamento_eliminar, medicamento_listar, medicamento_sumar, medicamento_restar

urlpatterns = [ 
    path('', medicamento, name = 'medicamentos'),
    path('listar/', medicamento_listar, name = 'medicamentos-listar'),
    path('crear/', medicamento_crear, name = 'medicamentos-crear'),
    path('editar/<int:pk>/', medicamento_editar, name = 'medicamentos-editar'),
    path('eliminar/<int:pk>/', medicamento_eliminar, name = 'medicamentos-eliminar'),
    path('sumar/<int:pk>/', medicamento_sumar, name = 'medicamentos-sumar'),
    path('restar/<int:pk>/', medicamento_restar, name = 'medicamentos-restar')
]