# Generated by Django 4.2.6 on 2023-10-20 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroDispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
                ('laboratorio', models.CharField(max_length=100)),
                ('dispositivo', models.CharField(max_length=100)),
                ('identificacao_dispositivo', models.CharField(max_length=50)),
                ('especificacoes_tecnicas', models.TextField()),
                ('data_aquisicao', models.DateField()),
                ('tipo_dispositivo', models.CharField(choices=[('notebook', 'Notebook'), ('computador', 'Computador'), ('datashow', 'Datashow'), ('monitor', 'Monitor'), ('mesa', 'Mesa'), ('cadeira', 'Cadeira'), ('impressora', 'Impressora')], default='notebook', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code_url', models.URLField()),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.cadastrodispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='Falha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
                ('laboratorio', models.CharField(max_length=100)),
                ('tipo_manutencao', models.CharField(max_length=50)),
                ('identificacao_dispositivo', models.CharField(max_length=50)),
                ('descricao_falha', models.TextField()),
                ('data_ocorrencia', models.DateField()),
                ('protocolo', models.CharField(max_length=10)),
                ('data_geracao', models.DateTimeField(auto_now_add=True)),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.cadastrodispositivo')),
            ],
        ),
        migrations.AddField(
            model_name='cadastrodispositivo',
            name='sala',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.sala'),
        ),
    ]