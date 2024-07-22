from django.urls import path
from . import views
from . views import VRegistro,cerrar_sesion,Logear

urlpatterns=[
    path('',VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('Logear/',Logear, name="Logear"),
]
