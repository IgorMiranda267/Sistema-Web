from django.shortcuts import render, redirect, get_object_or_404
from .models import CadastroDispositivo, Falha
from .forms import FormCadastroDispositivo, FormFalha
from django.utils.dateformat import DateFormat
import qrcode
from io import BytesIO
from django.core.files import File
from django.shortcuts import render, redirect
from .forms import FormCadastroDispositivo
from .models import CadastroDispositivo, QRCode
import random
import string

def gerar_protocolo(length=6):
    caracteres_permitidos = string.ascii_uppercase + string.digits
    protocolo = ''.join(random.choice(caracteres_permitidos) for _ in range(length))

    return protocolo

def cadastro_dispositivo(request):
    if request.method == 'POST':
        form = FormCadastroDispositivo(request.POST)
        if form.is_valid():
            novo_dispositivo = form.save()

            # Gere o QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(f'URL_PARA_DETALHES_DO_DISPOSITIVO/{novo_dispositivo.id}/')
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)

            # Crie um objeto QRCode associado ao dispositivo
            qr_code_obj = QRCode(dispositivo=novo_dispositivo, qr_code_url='URL_PARA_O_ARQUIVO_DO_QR_CODE')
            qr_code_obj.save()

            print("Novo dispositivo salvo com sucesso:", novo_dispositivo)
            return redirect('pagina_inicial')
        else:
            print("Erros no formulário:", form.errors)
    else:
        form = FormCadastroDispositivo()
    return render(request, 'cadastro/cadastro_dispositivo.html', {'form': form})

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
            falha = form.save(commit=False)
            falha.protocolo = gerar_protocolo()
            falha.save()
            return redirect('listar_falhas')
    else:
        form = FormFalha()

    return render(request, 'cadastro/cadastrar_falha.html', {'form': form, 'dispositivos': dispositivos})

def listar_falhas(request):
    falhas = Falha.objects.all()
    return render(request, 'cadastro/listar_falhas.html', {'falhas': falhas})

def listar_dispositivos_e_falhas(request):
    dispositivos = CadastroDispositivo.objects.all()
    return render(request, 'cadastro/listar_dispositivos_e_falhas.html', {'dispositivos': dispositivos})





