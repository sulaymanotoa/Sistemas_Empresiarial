from django.contrib import admin
from.models import Empleado,Salario,Resgistros

admin.site.register(Empleado,)
class EmpleadoAdmin(admin.ModelAdmin):
 list_display = ('id', 'nombre', 'apellido', 'edad', 'puesto', 'salario', ) 
 search_fields = ('id','nombre', 'apellido')
 list_filter = ('id','apellido')

admin.site.register(Salario,)
class SalarioAdmin(admin.ModelAdmin):
 list_display = ('empleado', 'mes', 'aumento', ) 
 search_fields = ('empleado','mes', )
 list_filter = ('empleado','aumento')

admin.site.register(Resgistros,)
class RegistrosAdmin(admin.ModelAdmin):
 list_display = ('empleado', 'fecha', 'observaciones') 
 search_fields = ('empleado','fecha',)
 list_filter = ('empleado','observaciones')
