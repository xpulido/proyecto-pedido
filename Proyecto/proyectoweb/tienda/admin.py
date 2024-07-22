from django.contrib import admin
from tienda.models import CategoriaPro,Producto

class CategoriaProAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'update')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'update')

admin.site.register(CategoriaPro,CategoriaProAdmin)
admin.site.register(Producto,ProductoAdmin)

