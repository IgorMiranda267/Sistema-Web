from django import forms
from .models import CadastroDispositivo

from django import forms
from .models import CadastroDispositivo

class FormCadastroDispositivo(forms.ModelForm):
    class Meta:
        model = CadastroDispositivo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormCadastroDispositivo, self).__init__(*args, **kwargs)
        
        # Adicione classes CSS aos widgets aqui
        self.fields['dispositivo'].widget.attrs['class'] = 'sua-classe-css'
        self.fields['identificacao_dispositivo'].widget.attrs['class'] = 'sua-classe-css'
        self.fields['especificacoes_tecnicas'].widget.attrs['class'] = 'sua-classe-css'
        self.fields['data_aquisicao'].widget.attrs['class'] = 'sua-classe-css'
