from django.forms import ModelForm
from eps.models import Eps

class EpsForm(ModelForm):
    class Meta:
        model = Eps
        fields = '__all__'
        # exclude = ['estado']