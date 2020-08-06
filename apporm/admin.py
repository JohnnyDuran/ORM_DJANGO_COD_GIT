from django.contrib import admin
from .models import Producto,Cliente,Factura,DetalleFactura
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion']
    list_display = ('descripcion','precio','stock','iva','creacion')
    ordering = ('descripcion',)
    search_fields = ('descripcion',)
    list_filter = ('descripcion',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)

#Para ingresar como administrador
#usuario: johnny
#password: johnny