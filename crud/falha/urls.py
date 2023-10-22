from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_falha/', views.cadastrar_falha, name='cadastro_falha'),
    path('cadastro_falha/<int:dispositivo_id>/', views.cadastrar_falha, name='cadastro_falha_dispositivo'),
    path('listar_falhas', views.listar_falhas, name='listar_falhas'),
    path('manutencao/cadastrar/', views.cadastrar_manutencao, name='cadastrar_manutencao'),
    path('manutencao/cadastrar/<int:falha_id>/', views.cadastrar_manutencao, name='cadastrar_faha_manutencao'),
    path('manutencao/listar/', views.listar_manutencoes, name='listar_manutencoes'),
    path('manutencao/editar/<int:manutencao_id>/', views.editar_manutencao, name='editar_manutencao'),
    path('manutencao/atualizar-status/<int:manutencao_id>/', views.atualizar_status_manutencao, name='atualizar_status_manutencao'),
]