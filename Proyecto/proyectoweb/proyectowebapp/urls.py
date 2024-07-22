from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home,name='home'),
    path('servicios/',views.servicios, name='servicios'),
    #path('tienda/',views.tienda, name='tienda'),
    # path('blog/',views.blog, name='blog'),
    path('contacto/',views.contacto, name='contacto'),
    path('mostrar_contacto/',views.mostrarcontacto, name='mostrarcontacto')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)