from django.urls import path
from basedatos.views import basedatos, respaldarbd, recuperarbd 

urlpatterns = [ 
    path('', basedatos, name = 'basedatos'),
    path('respaldarbd/', respaldarbd, name = 'respaldarbd'),
    path('recuperarbd/', recuperarbd, name = 'recuperarbd')
]