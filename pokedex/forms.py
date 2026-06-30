from django import forms
from .models import Pokemon
from .models import Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'weight': 'Peso',
            'height': 'Altura',
            'trainer': 'Entrenador',
            'picture': 'Imagen',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__' # Esto tomará de forma automática todos los campos de tu modelo Trainer        