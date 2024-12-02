from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import MovieViewSet

# Создаем роутер для API
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [
    # Панель администратора
    path('admin/', admin.site.urls),

    # Все API под /api/
    path('api/', include(router.urls)),
]
