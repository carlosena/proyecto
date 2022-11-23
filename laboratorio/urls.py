from django.urls import path 
from laboratorio.views import laboratorio, laboratorio_crear, laboratorio_editar, laboratorio_eliminar, laboratorio_listar

urlpatterns = [
    path('', laboratorio, name = 'laboratorio'),
    path('listar/', laboratorio_listar, name = "laboratorio-listar"),
    path('crear/', laboratorio_crear, name = 'laboratorio-crear'),
    path('editar/<int:pk>/', laboratorio_editar, name = 'laboratorio-editar'),
    path('eliminar/<int:pk>/', laboratorio_eliminar, name = 'laboratorio-eliminar')    
]