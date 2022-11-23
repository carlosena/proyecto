from django.urls import path
from nacionalidad.views import nacionalidad, nacionalidad_crear, nacionalidad_editar, nacionalidad_eliminar, nacionalidad_listar

urlpatterns = [ 
    path('', nacionalidad, name = 'nacionalidades'),
    path('crear/', nacionalidad_crear, name = 'nacionalidades-crear'),
    path('editar/<int:pk>/', nacionalidad_editar, name = 'nacionalidades-editar'),
    path('eliminar/<int:pk>/', nacionalidad_eliminar, name = 'nacionalidades-eliminar'),
    path('listar/', nacionalidad_listar, name = 'nacionalidades-listar')
]