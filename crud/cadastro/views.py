# cadastro/views.py
from django.shortcuts import render, redirect
from .models import CadastroDispositivo
from .forms import FormCadastroDispositivo  # Importe o formulário adequado

def pagina_inicial(request):
    if request.method == 'POST':
        form = FormCadastroDispositivo(request.POST)
        if form.is_valid():
            form.save()
            # Redirecione após o cadastro bem-sucedido
            return redirect('pagina_inicial')  # Você pode ajustar o nome da rota conforme necessário
    else:
        form = FormCadastroDispositivo()
    
    return render(request, 'cadastro/pagina_inicial.html', {'form': form})

# cadastro/views.py
from django.shortcuts import render, redirect
from .forms import FormCadastroDispositivo

def cadastro_dispositivo(request):
    if request.method == 'GET':
        form = FormCadastroDispositivo()
        return render(request, 'cadastro/cadastro_dispositivo.html', {'form': form})
    elif request.method == 'POST':
        form = FormCadastroDispositivo(request.POST)
        if form.is_valid():
            novo_dispositivo = form.save()
            print("Novo dispositivo salvo com sucesso:", novo_dispositivo)
            return redirect('pagina_inicial')  # Redirecione após o cadastro bem-sucedido
        else:
            print("Erros no formulário:", form.errors)
    return render(request, 'cadastro/cadastro_dispositivo.html', {'form': form})




