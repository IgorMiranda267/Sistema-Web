from django.urls import path
from . import views

urlpatterns = [

   path('', views.cadastro_dispositivo, name='cadastro_dispositivo'),
   
   path('listar_dispositivos_e_falhas', views.listar_dispositivos_e_falhas, name='listar_dispositivos_e_falhas'),
   
   path('editar_dispositivo/<int:dispositivo_id>/', views.editar_dispositivo, name='editar_dispositivo'),

   path('excluir_dispositivo/<int:dispositivo_id>/', views.excluir_dispositivo, name='excluir_dispositivo'),
   
   path('detalhes/<int:dispositivo_id>/', views.detalhes_dispositivo, name='detalhes_dispositivo'),
   
   path('imprimir_qr_code/<int:dispositivo_id>/', views.imprimir_qr_code, name='imprimir_qr_code'),
]
