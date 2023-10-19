from django.contrib import admin
from .models import CadastroDispositivo, Falha

# Register your models here.
class CadastroDispositivoAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'laboratorio', 'dispositivo', 'identificacao_dispositivo', 'data_aquisicao')
    search_fields = ('departamento', 'laboratorio', 'dispositivo', 'identificacao_dispositivo')
    list_filter = ('departamento', 'laboratorio', 'data_aquisicao')

class FalhaAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'laboratorio', 'tipo_manutencao', 'dispositivo', 'identificacao_dispositivo', 'data_ocorrencia')
    search_fields = ('departamento', 'laboratorio', 'dispositivo__dispositivo', 'identificacao_dispositivo', 'data_ocorrencia')
    list_filter = ('departamento', 'laboratorio', 'tipo_manutencao', 'data_ocorrencia')

admin.site.register(CadastroDispositivo, CadastroDispositivoAdmin)
admin.site.register(Falha, FalhaAdmin)

