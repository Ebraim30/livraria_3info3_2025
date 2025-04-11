from django.contrib import admin
from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet, CategoriaViewSet, EditoraViewSet, AutorViewSet

router = DefaultRouter()

router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autor", AutorViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
