from django.db import models

class Manutencao(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    dispositivo = models.CharField(max_length=100) 
    descricao = models.TextField()  
    data_ocorrencia = models.DateField()  
    descricao_falha = models.TextField()

    def __str__(self):
        return f"Manutenção em {self.dispositivo} em {self.data_ocorrencia}"

class Falha(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    tipo_manutencao = models.CharField(max_length=50)
    manutencao = models.ForeignKey(Manutencao, on_delete=models.CASCADE)
    identificacao_dispositivo = models.CharField(max_length=50)
    descricao_falha = models.TextField()
    data_ocorrencia = models.DateField()

    def __str__(self):
        return f'Falha em {self.manutencao.dispositivo} - {self.data_ocorrencia}'
