from django.db import models
from dispositivo.models import CadastroDispositivo

# Create your models here.

class Falha(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    tipo_manutencao = models.CharField(max_length=50)
    dispositivo = models.ForeignKey(CadastroDispositivo, on_delete=models.CASCADE)
    identificacao_dispositivo = models.CharField(max_length=50)
    descricao_falha = models.TextField()
    data_ocorrencia = models.DateField()
    protocolo = models.CharField(max_length=10) 
    data_geracao = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Falha em {self.dispositivo.nome} - {self.data_ocorrencia}'