# cadastro/urls.py
from django.urls import path
from .views import *

urlpatterns = [

   path('', pagina_inicial, name='pagina_inicial'),
   path('login/', login_view, name='login'),
   path("register/", register, name="register"),
   path('logout/', logout_view, name='logout'),
    path('redefinir-senha/', change_password_request, name='change_password_request'),
    path('redefinir-senha/confirmar/<str:uidb64>/<str:token>/', change_password_confirm, name='change_password_confirm'),
   path('confirmar-email/<str:token>/', confirm_email, name='confirm_email'),
    path('admin_approval_page/', admin_approval_page, name='admin_approval_page'),
   path('admin_approval_page/', admin_approval_page, name='admin_approval_page'),
    path('approve_user/<int:user_id>/', approve_user, name='approve_user'),  

]