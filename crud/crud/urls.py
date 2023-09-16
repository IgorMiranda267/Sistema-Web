from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/cadastro/start', permanent=False)),
    path('admin/', admin.site.urls),
    path('historico/', include('historico.urls')),  
    path('cadastro/', include('cadastro.urls')),
]