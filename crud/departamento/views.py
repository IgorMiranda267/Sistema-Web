from django.contrib.auth.decorators import login_required
from .forms import FormCadastroSala
from .models import Sala
from django.shortcuts import get_object_or_404, render, redirect

@login_required
def cadastro_sala(request):
    if request.method == 'POST':
        form = FormCadastroSala(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_salas')
        else:
            print("Erros no formulário:", form.errors)
    else:
        form = FormCadastroSala()
    return render(request, 'departamento/cadastro_sala.html', {'form': form})

@login_required
def editar_sala(request, sala_id):
    sala = get_object_or_404(Sala, pk=sala_id)
    if request.method == 'POST':
        form = FormCadastroSala(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('listar_salas')
    else:
        form = FormCadastroSala(instance=sala)
    return render(request, 'departamento/editar_sala.html', {'form': form})

@login_required
def excluir_sala(request, sala_id):
    sala = get_object_or_404(Sala, pk=sala_id)
    if request.method == 'POST':
        sala.delete()
        return redirect('listar_salas')
    return render(request, 'departamento/excluir_sala.html', {'sala': sala})

@login_required
def listar_salas(request):
    salas = Sala.objects.all()
    return render(request, 'departamento/listar_salas.html', {'salas': salas})
