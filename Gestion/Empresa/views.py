from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado, Salario, Resgistros
from .serializers import EmpleadoSerializer, SalarioSerializer, RegistrosSerializer
from rest_framework.permissions import AllowAny

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]
class SalarioViewSet(viewsets.ModelViewSet):
    queryset = Salario.objects.all()
    serializer_class = SalarioSerializer
    permission_classes = [AllowAny]
class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Resgistros.objects.all()
    serializer_class = RegistrosSerializer
    permission_classes = [AllowAny]