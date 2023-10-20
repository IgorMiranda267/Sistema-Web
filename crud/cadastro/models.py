from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.nome

from django.utils import timezone
class CadastroDispositivo(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    dispositivo = models.CharField(max_length=100)
    identificacao_dispositivo = models.CharField(max_length=50)
    especificacoes_tecnicas = models.TextField()
    data_aquisicao = models.DateField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    TIPOS_DE_DISPOSITIVO = (
        ('notebook', 'Notebook'),
        ('computador', 'Computador'),
        ('datashow', 'Datashow'),
        ('monitor', 'Monitor'),
        ('mesa', 'Mesa'),
        ('cadeira', 'Cadeira'),
        ('impressora', 'Impressora'),
    )

    tipo_dispositivo = models.CharField(
        max_length=20,
        choices=TIPOS_DE_DISPOSITIVO,
        default='notebook',
    )

    def __str__(self):
        return f'{self.departamento} - {self.laboratorio} - {self.dispositivo}'
        
class Falha(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    tipo_manutencao = models.CharField(max_length=50)
    dispositivo = models.ForeignKey('CadastroDispositivo', on_delete=models.CASCADE)
    identificacao_dispositivo = models.CharField(max_length=50)
    descricao_falha = models.TextField()
    data_ocorrencia = models.DateField()
    protocolo = models.CharField(max_length=10) 
    data_geracao = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Falha em {self.dispositivo.nome} - {self.data_ocorrencia}'

class QRCode(models.Model):
    dispositivo = models.ForeignKey(CadastroDispositivo, on_delete=models.CASCADE)
    qr_code_url = models.URLField()

    def __str__(self):
        return f'QR Code para {self.dispositivo}'
