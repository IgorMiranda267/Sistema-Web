from django.shortcuts import render, redirect, get_object_or_404
from dispositivo.views import gerar_protocolo
from .models import Falha, Manutencao
from .forms import FalhaForm, FormManutencao
from django.contrib.auth.decorators import login_required
from home.decorator import user_has_permission

@login_required
@user_has_permission('falha.add_falha')
def cadastrar_falha(request, dispositivo_id=None):
    if request.method == 'POST':
        form = FalhaForm(request.POST)
        if form.is_valid():
            falha = form.save(commit=False)
            falha.protocolo = gerar_protocolo()
            falha.save()
            return redirect('listar_falhas')
    else:
        if dispositivo_id:
            form = FalhaForm(initial={'dispositivo': dispositivo_id})
        else:
            form = FalhaForm()

    return render(request, 'falha/cadastrar_falha.html', {'form': form})

 
@login_required   
@user_has_permission('falha.view_falha')
def listar_falhas(request):
    falhas_com_manutencao = []

    for falha in Falha.objects.all():
        try:
            manutencao = Manutencao.objects.get(falha=falha)
            falha_com_manutencao = {
                'falha': falha,
                'manutencao': manutencao,
            }
            falhas_com_manutencao.append(falha_com_manutencao)
        except Manutencao.DoesNotExist:
            falha_com_manutencao = {
                'falha': falha,
                'manutencao': None,
            }
            falhas_com_manutencao.append(falha_com_manutencao)

    return render(request, 'falha/listar_falhas.html', {'falhas': falhas_com_manutencao})

@login_required
@user_has_permission('falha.add_manutencao')
def cadastrar_manutencao(request, falha_id=None):
    falha = None
    if falha_id:
        try:
            falha = Falha.objects.get(pk=falha_id)
        except Falha.DoesNotExist:
            pass

    if request.method == 'POST':
        form = FormManutencao(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.protocolo = gerar_protocolo()
            manutencao.falha = falha
            manutencao.save()

            return redirect('listar_manutencoes')
    else:
        form = FormManutencao()

    return render(request, 'falha/cadastrar_manutencao.html', {'manutencao_form': form, 'falha': falha, 'falha_id': falha_id})

@login_required
@user_has_permission('falha.view_manutencao')
def listar_manutencoes(request):
    manutencoes = Manutencao.objects.all()
    return render(request, 'falha/listar_manutencoes.html', {'manutencoes': manutencoes})

@login_required
@user_has_permission('falha.change_manutencao')
def editar_manutencao(request, manutencao_id):
    manutencao = get_object_or_404(Manutencao, pk=manutencao_id)
    if request.method == 'POST':
        form = FormManutencao(request.POST, instance=manutencao)
        if form.is_valid():
            form.save()
            return redirect('listar_manutencoes')
    else:
        form = FormManutencao(instance=manutencao)
        print(manutencao)
        print(form)
    return render(request, 'falha/editar_manutencao.html', {'form': form, 'manutencao': manutencao})

@login_required
@user_has_permission('falha.change_manutencao')
def atualizar_status_manutencao(request, manutencao_id):
    manutencao = get_object_or_404(Manutencao, pk=manutencao_id)
    if request.method == 'POST':
        form = FormManutencao(request.POST, instance=manutencao)
        if form.is_valid():
            form.save()
            return redirect('listar_manutencoes')
    else:
        form = FormManutencao(instance=manutencao)

    return render(request, 'falha/atualizar_status_manutencao.html', {'form': form, 'manutencao': manutencao})

