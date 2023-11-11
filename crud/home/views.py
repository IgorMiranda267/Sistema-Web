from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User 
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .forms import RegisterForm
from .models import CustomUser
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import user_passes_test

def pagina_inicial(request):
    
    return render(request, 'home/pagina_inicial.html')

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pagina_inicial'))
    
    next_url = request.GET.get('next')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user.email_confirmed == False:
                messages.error(request, 'Email não confirmado! Por favor, confirme o seu cadastro.')
            else:   
                if user is not None:
                    login(request, user)
                    if next_url:
                        return redirect(next_url)
                    return redirect('pagina_inicial')
                else:
                    messages.error(request, 'Usuário ou senha incorretos')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

def change_password_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            token = default_token_generator.make_token(user)

            reset_url = request.build_absolute_uri(
                reverse('change_password_confirm', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': token})
            )

            subject = 'Redefinir Senha'
            message = render_to_string('home/reset_password_email.html', {'reset_url': reset_url})
            from_email = 'your_email@example.com'
            to_email = user.email
            send_mail(subject, message, from_email, [to_email])

            messages.success(request, 'Um link para redefinir a senha foi enviado para o seu e-mail.')
            return redirect('login')
        else:
            messages.error(request, 'Usuário não encontrado.')
    return render(request, 'home/change_password_request.html')

def change_password_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Senha alterada com sucesso. Faça login com sua nova senha.')
            return redirect('login')
        return render(request, 'home/change_password_confirm.html')
    else:
        messages.error(request, 'O link para redefinir a senha é inválido ou expirou.')
        return redirect('login')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            user_group, _ = Group.objects.get_or_create(name='Usuário')

            user.groups.add(user_group)
            
            confirmation_link = request.build_absolute_uri(reverse('confirm_email', args=[user.email_confirmation_token]))
            subject = 'Confirme seu endereço de e-mail'
            message = f'Por favor, clique no link a seguir para confirmar seu endereço de e-mail: {confirmation_link}'
            from_email = 'filmesapi24@gmail.com'  # Substitua pelo seu endereço de e-mail
            to_email = user.email
            send_mail(subject, message, from_email, [to_email])

            messages.success(request, 'Registro bem-sucedido! Um e-mail de confirmação foi enviado para o seu endereço.')
            return redirect("login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = RegisterForm()
    return render(request, "home/register.html", {"form": form})

def confirm_email(request, token):
    user = CustomUser.objects.filter(email_confirmation_token=token).first()
    
    if user:
        user.email_confirmed = True
        user.email_confirmation_token = None
        user.save()
        
        messages.success(request, 'Seu e-mail foi confirmado com sucesso!')
    else:
        messages.error(request, 'Token de confirmação inválido ou expirado.')

    return redirect("login")

def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')

@user_passes_test(lambda u: u.is_staff)
def approve_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_approved = True
    user.save()
    messages.success(request, 'Usuário aprovado com sucesso!')
    return redirect("admin_approval_page")  # Redireciona para a página que lista usuários aguardando aprovação

@user_passes_test(lambda u: u.is_staff)
def admin_approval_page(request):
    users_waiting_approval = CustomUser.objects.filter(is_approved=False)
    return render(request, 'home/admin_approval_page.html', {'users_waiting_approval': users_waiting_approval})