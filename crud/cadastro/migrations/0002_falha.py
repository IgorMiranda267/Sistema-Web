# Generated by Django 4.2.5 on 2023-09-17 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
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
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.cadastrodispositivo')),
            ],
        ),
    ]
