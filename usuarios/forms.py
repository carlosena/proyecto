from django.forms import ModelForm, widgets 
from usuarios.models import Usuario 

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        widgets= {
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        }
        exclude = ['user', 'foto', 'fechaCreacion']
        # fields = '__all__'
        
