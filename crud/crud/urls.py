from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Fix Flow API",
        default_version='v1',
        description="A API da Fix Flow permite o gerenciamento de dispositivos, falhas, manutenções e salas em ambientes corporativos. Esta API oferece recursos poderosos para facilitar a manutenção e controle de ativos em uma organização.",
        terms_of_service="https://www.fixflow.com/terms/",
        contact=openapi.Contact(email="contact@fixflow.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', RedirectView.as_view(url='/home/login', permanent=False)),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('falha/', include('falha.urls')),
    path('dispositivo/', include('dispositivo.urls')),
    path('departamento/', include('departamento.urls')),
    
    path('api/', include('api.urls')),
    #re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)