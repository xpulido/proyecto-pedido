from django.contrib import admin
from .models import Servicios, Contacto

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Servicios, ServiciosAdmin)

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Contacto, ContactoAdmin)