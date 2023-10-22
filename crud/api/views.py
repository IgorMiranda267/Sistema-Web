from rest_framework import viewsets
from .models import CadastroDispositivo, QRCode, Sala, Falha, Manutencao
from .serializers import (
    CadastroDispositivoSerializer, QRCodeSerializer,
    SalaSerializer, FalhaSerializer, ManutencaoSerializer
)

class CadastroDispositivoViewSet(viewsets.ModelViewSet):
    queryset = CadastroDispositivo.objects.all()
    serializer_class = CadastroDispositivoSerializer

class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class FalhaViewSet(viewsets.ModelViewSet):
    queryset = Falha.objects.all()
    serializer_class = FalhaSerializer

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
