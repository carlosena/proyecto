from django.forms import ModelForm
from familiar.models import Familiar 

class FamiliarForm(ModelForm):
    class Meta: 
        model = Familiar
        fields = '__all__'