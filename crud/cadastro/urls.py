# cadastro/urls.py
from django.urls import path
from . import views

urlpatterns = [

   path('', views.cadastro_dispositivo, name='cadastro_dispositivo'),
   
   path('listar_dispositivos_e_falhas', views.listar_dispositivos_e_falhas, name='listar_dispositivos_e_falhas'),
   
   path('editar_dispositivo/<int:dispositivo_id>/', views.editar_dispositivo, name='editar_dispositivo'),

   path('excluir_dispositivo/<int:dispositivo_id>/', views.excluir_dispositivo, name='excluir_dispositivo'),
   
   path('cadastro_falha', views.cadastrar_falha, name='cadastro_falha'),
   
   path('listar_falhas', views.listar_falhas, name='listar_falhas'),
   
]
