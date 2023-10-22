from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateformat import DateFormat
from .forms import FormCadastroDispositivo
from .models import CadastroDispositivo, QRCode
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from io import BytesIO
from django.urls import reverse
from departamento.models import Sala
from falha.models import Manutencao, Falha
from falha.forms import FormManutencao, FalhaForm
import qrcode
import base64
import random
import string
from django.contrib.auth.decorators import login_required

@login_required
def gerar_protocolo(length=6):
    caracteres_permitidos = string.ascii_uppercase + string.digits
    protocolo = ''.join(random.choice(caracteres_permitidos) for _ in range(length))
    return protocolo

@login_required
def cadastro_dispositivo(request):
    salas = Sala.objects.all()
    if request.method == 'POST':
        form = FormCadastroDispositivo(request.POST)
        if form.is_valid():
            novo_dispositivo = form.save()
            
            ip = request.META.get('REMOTE_ADDR')
            porta = request.META.get('SERVER_PORT')
            custom_domain = f"http://{ip}:{porta}"
            
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            detalhes_url = reverse('detalhes_dispositivo', args=[novo_dispositivo.id])
            full_url = f"{custom_domain}{detalhes_url}"
            qr.add_data(full_url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            
            file_name = f'qrcodes/qrcode_{novo_dispositivo.id}.png'
            default_storage.save(file_name, ContentFile(buffer.getvalue()))
            novo_dispositivo.qr_code = file_name
            novo_dispositivo.save()
            qr_code_obj = QRCode(dispositivo=novo_dispositivo, qr_code_base64=None)
            qr_code_obj.save()
            
            print("Novo dispositivo salvo com sucesso:", novo_dispositivo)
            return render(request, 'dispositivo/popup_qr_code.html', {'dispositivo': novo_dispositivo})
        else:
            print("Erros no formulário:", form.errors)
    else:
        form = FormCadastroDispositivo()
    return render(request, 'dispositivo/cadastro_dispositivo.html', {'form': form, 'salas': salas})

@login_required
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
    return render(request, 'dispositivo/editar_dispositivo.html', {'form': form})

@login_required
def excluir_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(CadastroDispositivo, pk=dispositivo_id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('listar_dispositivos_e_falhas')
    return render(request, 'dispositivo/excluir_dispositivo.html', {'dispositivo': dispositivo})

@login_required
def listar_dispositivos_e_falhas(request):
    dispositivos = CadastroDispositivo.objects.all()
    return render(request, 'dispositivo/listar_dispositivos_e_falhas.html', {'dispositivos': dispositivos})

@login_required
def detalhes_dispositivo(request, dispositivo_id):
    dispositivo = CadastroDispositivo.objects.get(pk=dispositivo_id)
    qr_code_obj = QRCode.objects.get(dispositivo=dispositivo)
    falhas = Falha.objects.filter(dispositivo=dispositivo)
    manutencoes = Manutencao.objects.filter(falha__dispositivo=dispositivo)
    if request.method == 'POST':
        falha_form = FalhaForm(request.POST, prefix='falha')
        manutencao_form = FormManutencao(request.POST, prefix='manutencao')
        if falha_form.is_valid():
            nova_falha = falha_form.save(commit=False)
            nova_falha.dispositivo = dispositivo
            nova_falha.save()
            falha_form = FalhaForm()
        elif manutencao_form.is_valid():
            nova_manutencao = manutencao_form.save(commit=False)
            nova_manutencao.dispositivo = dispositivo
            nova_manutencao.save()
            manutencao_form = FormManutencao()
    else:
        falha_form = FalhaForm(prefix='falha')
        manutencao_form = FormManutencao(prefix='manutencao')
    context = {
        'dispositivo': dispositivo,
        'qr_code_obj': qr_code_obj,
        'falhas': falhas,
        'falha_form': falha_form,
        'manutencoes': manutencoes,
        'manutencao_form': manutencao_form
    }
    return render(request, 'dispositivo/detalhes_dispositivo.html', context)

@login_required
def imprimir_qr_code(request, dispositivo_id):
    dispositivo = get_object_or_404(CadastroDispositivo, pk=dispositivo_id)
    qr_code_obj = QRCode.objects.get(dispositivo=dispositivo)
    qr_code_image = base64.b64decode(qr_code_obj.qr_code_base64.encode('utf-8'))
    response = HttpResponse(qr_code_image, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="qrcode_dispositivo_{dispositivo_id}.png"'
    return response
