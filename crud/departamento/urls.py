
from django.urls import path
from dispositivo import views

urlpatterns = [

   path('listar_dispositivos_e_falhas', views.listar_dispositivos_e_falhas, name='listar_dispositivos_e_falhas'),

]
