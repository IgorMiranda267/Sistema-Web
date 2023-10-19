from django.shortcuts import render, redirect, get_object_or_404
from .models import CadastroDispositivo, Falha
from .forms import FormCadastroDispositivo, FormFalha
from django.utils.dateformat import DateFormat

def cadastro_dispositivo(request):
    if request.method == 'GET':
        form = FormCadastroDispositivo()
        return render(request, 'cadastro/cadastro_dispositivo.html', {'form': form})
    elif request.method == 'POST':
        form = FormCadastroDispositivo(request.POST)
        if form.is_valid():
            novo_dispositivo = form.save()
            print("Novo dispositivo salvo com sucesso:", novo_dispositivo)
            return redirect('pagina_inicial')
        else:
            print("Erros no formulário:", form.errors)
    return render(request, 'cadastro/cadastro_dispositivo.html', {'form': form})

def listar_dispositivos_e_falhas(request):
    dispositivos = CadastroDispositivo.objects.all()
    return render(request, 'cadastro/listar_dispositivos_e_falhas.html', {'dispositivos': dispositivos})


def editar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(CadastroDispositivo, pk=dispositivo_id)
    if request.method == 'POST':
        form = FormCadastroDispositivo(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos_e_falhas')
    else:
        df = DateFormat(dispositivo.data_aquisicao)
        dispositivo.data_aquisicao = df.format('Y-m-d')
        form = dispositivo

    return render(request, 'cadastro/editar_dispositivo.html', {'form': form})

def excluir_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(CadastroDispositivo, pk=dispositivo_id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('listar_dispositivos_e_falhas')
    return render(request, 'cadastro/excluir_dispositivo.html', {'dispositivo': dispositivo})

def cadastrar_falha(request):
    dispositivos = CadastroDispositivo.objects.all()
    if request.method == 'POST':
        form = FormFalha(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_falhas')
    else:
        form = FormFalha()

    return render(request, 'cadastro/cadastrar_falha.html', {'form': form, 'dispositivos': dispositivos})


def listar_falhas(request):
    falhas = Falha.objects.all()
    return render(request, 'cadastro/listar_falhas.html', {'falhas': falhas})



