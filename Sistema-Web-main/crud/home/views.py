# cadastro/views.py
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages

def pagina_inicial(request):
    
    return render(request, 'home/pagina_inicial.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página inicial após o login bem-sucedido
                return redirect('pagina_inicial')
            else:
                # Adicionar uma mensagem de erro se a senha estiver incorreta
                messages.error(request, 'Usuário ou senha incorretos')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("pagina_inicial")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = RegisterForm()
    return render(request, "home/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')
