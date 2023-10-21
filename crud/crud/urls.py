from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/home/login', permanent=False)),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('falha/', include('falha.urls')),
    path('dispositivo/', include('dispositivo.urls')),
    path('departamento/', include('departamento.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)