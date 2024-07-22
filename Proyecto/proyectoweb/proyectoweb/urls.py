from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('proyectowebapp.urls')),
    path('blog/',include('blog.urls')),
    path('',include('tienda.urls')),
    path('carro/',include('carro.urls')), #re direcionar al carrito
    path('autenticacion/',include('autenticacion.urls')),
    path('pedidos/',include('pedidos.urls'))
    
]
