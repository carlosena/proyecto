from django.urls import path
from usuarios.views import usuarios, usuarios_crear, usuarios_editar, usuarios_eliminar, usuarios_listar, manual

urlpatterns = [ 
    path('', usuarios, name = 'usuarios'), 
    path('listar/', usuarios_listar, name = "usuarios-listar"),
    path('crear/', usuarios_crear, name = "usuarios-crear"),
    path('editar/<int:pk>/', usuarios_editar, name = "usuarios-editar"),
    path('eliminar/<int:pk>/', usuarios_eliminar, name = "usuarios-eliminar"),
    path('manual-usuario/', manual, name = 'manual'),
]