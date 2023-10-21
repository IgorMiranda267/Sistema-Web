
from django.contrib import admin
from .models import Falha

class FalhaAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'laboratorio', 'tipo_manutencao', 'dispositivo', 'identificacao_dispositivo', 'data_ocorrencia')
    search_fields = ('departamento', 'laboratorio', 'dispositivo__dispositivo', 'identificacao_dispositivo', 'data_ocorrencia')
    list_filter = ('departamento', 'laboratorio', 'tipo_manutencao', 'data_ocorrencia')

admin.site.register(Falha, FalhaAdmin)

