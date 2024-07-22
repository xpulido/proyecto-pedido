from django.urls import path
from . import views
from tienda.views import ReporteProductoExel

urlpatterns = [
    path('tienda/',views.tienda, name='Tienda'),
    path('reporte/',views.ReporteProductoExel.as_view(), name='reporte'),
    path('listado/',views.listado,name='listado'),
    path('pdf/',views.ListaProductoPdf.as_view(), name='pdf')

]