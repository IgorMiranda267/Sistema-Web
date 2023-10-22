from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CadastroDispositivoViewSet, QRCodeViewSet,
    SalaViewSet, FalhaViewSet, ManutencaoViewSet
)

router = DefaultRouter()
router.register(r'cadastrodispositivos', CadastroDispositivoViewSet)
router.register(r'qrcodes', QRCodeViewSet)
router.register(r'salas', SalaViewSet)
router.register(r'falhas', FalhaViewSet)
router.register(r'manutencoes', ManutencaoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
