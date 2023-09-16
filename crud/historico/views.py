from django.shortcuts import render
from .models import Manutencao, Falha

def listar_manutencoes(request):
    manutencoes = Manutencao.objects.all()
    return render(request, 'listar_manutencoes.html', {'manutencoes': manutencoes})

def listar_falhas(request):
    falhas = Falha.objects.all()
    return render(request, 'listar_falhas.html', {'falhas': falhas})