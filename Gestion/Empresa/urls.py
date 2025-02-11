from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, SalarioViewSet, RegistrosViewSet

router = DefaultRouter()
router.register(r'Empleados', EmpleadoViewSet)
router.register(r'Salario', SalarioViewSet)
router.register(r'Registros',RegistrosViewSet)

# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]