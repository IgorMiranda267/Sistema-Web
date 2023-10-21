from django.shortcuts import render, redirect
from dispositivo.models import CadastroDispositivo
from dispositivo.views import gerar_protocolo
from .models import Falha
from .forms import FormFalha

def cadastrar_falha(request):
    dispositivos = CadastroDispositivo.objects.all()
    if request.method == 'POST':
        form = FormFalha(request.POST)
        if form.is_valid():
            falha = form.save(commit=False)
            falha.protocolo = gerar_protocolo()
            falha.save()
            return redirect('listar_falhas')
    else:
        form = FormFalha()

    return render(request, 'falha/cadastrar_falha.html', {'form': form, 'dispositivos': dispositivos})

def listar_falhas(request):
    falhas = Falha.objects.all()
    return render(request, 'falha/listar_falhas.html', {'falhas': falhas})

