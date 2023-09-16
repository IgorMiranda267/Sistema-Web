from django.urls import path
from . import views

urlpatterns = [
    path('listar_manutencoes/', views.listar_manutencoes, name='listar_manutencoes'),
    path('listar_falhas/', views.listar_falhas, name='listar_falhas'),
]
