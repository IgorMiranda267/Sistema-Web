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
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from django.urls import reverse

def gerar_protocolo(length=6):
    caracteres_permitidos = string.ascii_uppercase + string.digits
    protocolo = ''.join(random.choice(caracteres_permitidos) for _ in range(length))

    return protocolo

import qrcode
import base64

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def cadastro_dispositivo(request):
    if request.method == 'POST':
        form = FormCadastroDispositivo(request.POST)
        if form.is_valid():
            novo_dispositivo = form.save()

            # Domínio personalizado
            custom_domain = "http://site"  # Substitua pelo seu domínio real
            
            # Gere o QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            # Gere a URL real para a página de detalhes do dispositivo usando a reversão de URL
            detalhes_url = reverse('detalhes_dispositivo', args=[novo_dispositivo.id])
            
            # Construa a URL completa com o domínio personalizado
            full_url = f"{custom_domain}{detalhes_url}"
            
            qr.add_data(full_url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            # Salve o QR code na pasta 'qrcodes' dentro de 'media'
            file_name = f'qrcodes/qrcode_{novo_dispositivo.id}.png'
            default_storage.save(file_name, ContentFile(buffer.getvalue()))

            # Atualize o campo qr_code do objeto CadastroDispositivo com o caminho do arquivo
            novo_dispositivo.qr_code = file_name
            novo_dispositivo.save()

            # Crie um objeto QRCode associado ao dispositivo
            qr_code_obj = QRCode(dispositivo=novo_dispositivo, qr_code_base64=None)  # Substitua por qr_code_base64, se necessário
            qr_code_obj.save()

            print("Novo dispositivo salvo com sucesso:", novo_dispositivo)
            return render(request, 'cadastro/popup_qr_code.html', {'dispositivo': novo_dispositivo})
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

def detalhes_dispositivo(request, dispositivo_id):
    dispositivo = CadastroDispositivo.objects.get(pk=dispositivo_id)
    qr_code_obj = QRCode.objects.get(dispositivo=dispositivo)
    return render(request, 'cadastro/detalhes_dispositivo.html', {'dispositivo': dispositivo, 'qr_code_obj': qr_code_obj})


import base64

def imprimir_qr_code(request, dispositivo_id):
    dispositivo = get_object_or_404(CadastroDispositivo, pk=dispositivo_id)
    qr_code_obj = QRCode.objects.get(dispositivo=dispositivo)

    # Converta a imagem do QR Code de base64 para bytes
    qr_code_image = base64.b64decode(qr_code_obj.qr_code_base64.encode('utf-8'))

    # Defina o tipo de resposta
    response = HttpResponse(qr_code_image, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="qrcode_dispositivo_{dispositivo_id}.png"'

    return response







