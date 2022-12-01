from django.forms import ModelForm
from paciente.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        #fields = '__all__'
        exclude = ['fechaCreacion']