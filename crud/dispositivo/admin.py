from django.contrib import admin
from .models import CadastroDispositivo

# Register your models here.
class CadastroDispositivoAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'laboratorio', 'dispositivo', 'identificacao_dispositivo', 'data_aquisicao')
    search_fields = ('departamento', 'laboratorio', 'dispositivo', 'identificacao_dispositivo')
    list_filter = ('departamento', 'laboratorio', 'data_aquisicao')

admin.site.register(CadastroDispositivo, CadastroDispositivoAdmin)
