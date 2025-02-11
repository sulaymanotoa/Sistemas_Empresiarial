from rest_framework import serializers
from.models import Empleado, Salario, Resgistros

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
class SalarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salario
        fields = '__all__'
class RegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resgistros
        fields = '__all__'

        