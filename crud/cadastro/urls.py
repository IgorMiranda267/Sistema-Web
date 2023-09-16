# cadastro/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Outras rotas do seu aplicativo

    # Rota para a página de cadastro
    path('', views.cadastro_dispositivo, name='cadastro_dispositivo'),
   path('start', views.pagina_inicial, name='pagina_inicial'), 

]
