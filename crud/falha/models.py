from django.db import models
from dispositivo.models import CadastroDispositivo

class Falha(models.Model):
    dispositivo = models.ForeignKey(CadastroDispositivo, on_delete=models.CASCADE)
    descricao_falha = models.TextField()
    data_ocorrencia = models.DateField()
    data_geracao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Falha em {self.dispositivo} - {self.data_ocorrencia}'

    @classmethod
    def falhas_por_dispositivo(cls, dispositivo):
        return cls.objects.filter(dispositivo=dispositivo).order_by('-data_ocorrencia')


class Manutencao(models.Model):
    TIPOS_DE_MANUTENCAO = (
        ('preventiva', 'Preventiva'),
        ('corretiva', 'Corretiva'),
        ('preditiva', 'Preditiva'),
    )

    STATUS = (
        ('nao_iniciado', 'Não Iniciado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    )

    tipo_manutencao = models.CharField(max_length=50, choices=TIPOS_DE_MANUTENCAO)
    materiais_utilizados = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS)
    data_finalizacao = models.DateField(null=True, blank=True)
    protocolo = models.CharField(max_length=10, unique=True)
    
    falha = models.OneToOneField(Falha, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.protocolo} - {self.get_status_display()}"
