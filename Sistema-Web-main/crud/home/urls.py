# cadastro/urls.py
from django.urls import path
from . import views
from .views import register
from .views import logout_view

urlpatterns = [

   path('', views.pagina_inicial, name='pagina_inicial'),
   path('login/', views.login_view, name='login'),
   path("register/", register, name="register"),
   path('logout/', logout_view, name='logout'),
   
]
