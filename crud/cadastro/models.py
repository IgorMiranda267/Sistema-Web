from django.db import models

class CadastroDispositivo(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    dispositivo = models.CharField(max_length=100)
    identificacao_dispositivo = models.CharField(max_length=50)
    especificacoes_tecnicas = models.TextField()
    data_aquisicao = models.DateField()
    
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

    def _str_(self):
        return f'Falha em {self.dispositivo.nome} - {self.data_ocorrencia}'
