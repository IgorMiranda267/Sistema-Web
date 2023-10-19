from django import forms
from .models import CadastroDispositivo
from .models import Falha

class FormCadastroDispositivo(forms.ModelForm):
    class Meta:
        model = CadastroDispositivo
        fields = '__all__'

    widgets = {
        'data_aquisicao': forms.DateInput(attrs={'type': 'date'}),
    }

class FormFalha(forms.ModelForm):
    class Meta:
        model = Falha
        fields = '__all__'
