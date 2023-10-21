
from django.urls import path
from departamento import views

urlpatterns = [

   path('departamento/cadastrar/', views.cadastro_sala, name='cadastro_sala'),
   path('departamento/editar/<int:sala_id>/', views.editar_sala, name='editar_sala'),
   path('departamento/excluir/<int:sala_id>/', views.excluir_sala, name='excluir_sala'),
   path('departamento/listar/', views.listar_salas, name='listar_salas'),

]
