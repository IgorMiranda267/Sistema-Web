from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_falha', views.cadastrar_falha, name='cadastro_falha'),
    path('listar_falhas', views.listar_falhas, name='listar_falhas'),
]