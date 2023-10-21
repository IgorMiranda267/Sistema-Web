from django import forms
from .models import Falha

class FormFalha(forms.ModelForm):
    class Meta:
        model = Falha
        fields = '__all__'
