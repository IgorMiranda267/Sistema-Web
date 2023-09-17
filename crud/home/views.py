# cadastro/views.py
from django.shortcuts import render, redirect

def pagina_inicial(request):
    
    return render(request, 'home/pagina_inicial.html')




