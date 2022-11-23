from django.urls import path
from familiar.views import familiar, familiar_crear, familiar_editar, familiar_eliminar, familiar_listar 

urlpatterns = [ 
    path('', familiar, name = 'familiar'),
    path('listar/', familiar_listar, name = 'familiar-listar'),
    path('crear/', familiar_crear, name = 'familiar-crear'),
    path('editar/<int:pk>/', familiar_editar, name = 'familiar-editar'),
    path('eliminar/<int:pk>/', familiar_eliminar, name = 'familiar-eliminar')
]