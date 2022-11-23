from django.urls import path 
from formula.views import formula 

urlpatterns = [ 
    path('', formula, name = 'formula')
]