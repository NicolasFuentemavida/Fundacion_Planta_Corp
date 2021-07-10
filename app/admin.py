from app.forms import ProductoForm
from app.models import *
from django.contrib import admin


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','categoria','imagen',]
    list_editable = ['stock','descripcion']
    search_fields = ['codigo']
    list_per_page = 5
    list_filter = ['categoria']
    form = ProductoForm

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','paterno','rut','direccion','telefono','mail',]
    search_fields = ['rut']
    list_per_page = 5

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria','id']
    search_fields = ['categoria']
    list_per_page = 5

class DescuentoAdmin(admin.ModelAdmin):
    list_display = ['codigo_descuento','valor_descuento']
    search_fields = ['categoria']
    list_per_page = 5

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['numero_pedido','fecha_pedido','iva']
    search_fields = ['categoria']
    list_per_page = 5

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ['nombre_proveedor','direccion','telefono','mail','numero_pedido']
    search_fields = ['categoria']
    list_per_page = 5


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedores,ProveedoresAdmin)
admin.site.register(Descuento,DescuentoAdmin)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Cliente,ClienteAdmin)