from django.forms import ModelForm
from medicamento.models import Medicamento

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        # fields = '__all__'
        exclude = ['consumoDiario', 'contador', 'alerta', 'fechaCreacion', 'ultimaDosis']


