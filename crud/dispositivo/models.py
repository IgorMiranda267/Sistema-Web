from django.db import models
from departamento.models import Sala

# Create your models here.
class CadastroDispositivo(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    dispositivo = models.CharField(max_length=100)
    identificacao_dispositivo = models.CharField(max_length=50)
    especificacoes_tecnicas = models.TextField()
    data_aquisicao = models.DateField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, default=None, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qrcodes/', null=True, blank=True)
    
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
    
class QRCode(models.Model):
    dispositivo = models.ForeignKey(CadastroDispositivo, on_delete=models.CASCADE)
    qr_code_base64 = models.TextField(null=True, blank=True)  # Campo para armazenar a imagem do QR Code em base64

    def __str__(self):
        return f'QR Code para {self.dispositivo}'