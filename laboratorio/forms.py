from django.forms import ModelForm 
from laboratorio.models import Laboratorio

class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        #fields = '__all__'
        exclude = ['fechaCreacion']