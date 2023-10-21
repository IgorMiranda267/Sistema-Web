from django.contrib import admin
from .models import CadastroDispositivo

# Register your models here.
class CadastroDispositivoAdmin(admin.ModelAdmin):
    list_display = ('sala', 'dispositivo', 'identificacao_dispositivo', 'data_aquisicao')
    search_fields = ('sala', 'dispositivo', 'identificacao_dispositivo')
    list_filter = ('sala', 'data_aquisicao')

admin.site.register(CadastroDispositivo, CadastroDispositivoAdmin)
