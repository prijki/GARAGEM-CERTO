from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, MarcaViewSet, CarroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'Marca', MarcaViewSet)
router.register(r'Carro', CarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]