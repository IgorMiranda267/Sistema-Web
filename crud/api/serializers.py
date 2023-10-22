from rest_framework import serializers
from .models import CadastroDispositivo, QRCode, Sala, Falha, Manutencao

class CadastroDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroDispositivo
        fields = '__all__'

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class FalhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Falha
        fields = '__all__'

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'
