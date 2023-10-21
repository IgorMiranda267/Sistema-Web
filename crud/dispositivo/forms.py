from django import forms
from .models import CadastroDispositivo

class FormCadastroDispositivo(forms.ModelForm):
    class Meta:
        model = CadastroDispositivo
        fields = '__all__'

    widgets = {
        'data_aquisicao': forms.DateInput(attrs={'type': 'date'}),
    }

