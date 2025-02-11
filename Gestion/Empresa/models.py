from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from . validadores import validacion_numeros, validar_nombres
from .choices import CARGO


class Empleado(models.Model):
    id = models.AutoField(primary_key=True,validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=20,validators=[MaxLengthValidator(50), validar_nombres])
    apellido = models.CharField(max_length=20,validators=[MaxLengthValidator(50), validar_nombres])
    edad = models.IntegerField()
    puesto = models.CharField(max_length=50, choices=CARGO)
    class Meta:
       verbose_name = 'Empleado'
       verbose_name_plural = 'Empleados'
       db_table = 'empleado'
def __str__(self):
            return self.nombre + ' ' + self.apellido
       
class Salario(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  mes = models.CharField(max_length=10)
  aumento = models.DecimalField(max_digits=10, decimal_places=2)
  class Meta:
        verbose_name = 'Salario'
        verbose_name_plural = 'Salarios'
        db_table ='salario'
def __str__(self):
            return self.empleado.nombre + ' ' + self.mes
class Resgistros (models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  fecha = models.DateField()
  observaciones = models.TextField()
  class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        db_table ='registro'
def __str__(self):
            return self.empleado.nombre + ' ' + str(self.fecha)

    
