from django.forms import ModelForm
from cargo.models import Cargo

class CargoForm(ModelForm):
    class Meta: 
        model = Cargo
        fields = '__all__'
        # exclude = ['estado']