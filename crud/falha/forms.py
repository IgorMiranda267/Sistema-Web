from django import forms
from .models import Falha 

from django import forms
from .models import Falha, Manutencao
from dispositivo.models import CadastroDispositivo
from departamento.models import Sala
from django.forms import DateInput

from django import forms
from .models import Falha 

class FalhaForm(forms.ModelForm):
    
    dispositivo = forms.ModelChoiceField(queryset=CadastroDispositivo.objects.all(), empty_label="Selecione um dispositivo")

    class Meta:
        model = Falha
        fields = ['dispositivo', 'descricao_falha', 'data_ocorrencia']

    def __init__(self, *args, **kwargs):
        super(FalhaForm, self).__init__(*args, **kwargs)
        if 'data' in self.data:
            try:
                sala_id = int(self.data.get('sala'))
                dispositivo = CadastroDispositivo.objects.filter(sala=sala_id)
                self.fields['dispositivo'].queryset = dispositivo
            except (ValueError, TypeError):
                pass
class FormManutencao(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['tipo_manutencao', 'materiais_utilizados', 'status', 'data_finalizacao']

    data_finalizacao = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
