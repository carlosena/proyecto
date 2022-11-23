from django.forms import ModelForm
from nacionalidad.models import Nacionalidad 

class NacionalidadForm(ModelForm):
    class Meta: 
        model = Nacionalidad
        fields = '__all__'
        # exclude = ['estado']

        