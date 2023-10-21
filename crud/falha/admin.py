from django.contrib import admin
from .models import Falha, Manutencao

class FalhaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'data_ocorrencia')
    search_fields = ('dispositivo__dispositivo', 'data_ocorrencia')
    list_filter = ('data_ocorrencia',)  # Adicionada uma vírgula

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('protocolo', 'tipo_manutencao', 'materiais_utilizados', 'status', 'data_finalizacao', 'protocolo')
    search_fields = ('protocolo', 'tipo_manutencao', 'status', 'protocolo')
    list_filter = ('tipo_manutencao', 'status', 'data_finalizacao')

admin.site.register(Falha, FalhaAdmin)
admin.site.register(Manutencao, ManutencaoAdmin)
