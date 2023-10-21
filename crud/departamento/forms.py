from django import forms
from .models import Sala

class FormCadastroSala(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'
