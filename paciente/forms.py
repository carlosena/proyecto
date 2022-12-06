from django.forms import ModelForm, widgets
from paciente.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        #fields = '__all__'
        widgets={
            'fechaNacimiento': widgets.DateInput(attrs={'type':'date'})
            #'fechaNovedad': widgets.DateInput(attrs={'type':'date'})
        }
        exclude = ['fechaCreacion', 'tipoNovedad']