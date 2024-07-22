from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from carro.carro import Carro
from servicios.models import Servicios, Contacto
from proyectoweb.forms import FormularioContacto
from django.core.mail import EmailMessage
from django.core.paginator import Paginator

def home (request):
    carro = Carro(request)
    return render(request, "home.html", {})

def servicios (request):
    listado = Servicios.objects.all()
    paginator = Paginator(listado, 1)
    pagina = request.GET.get("page") or 1 #coge la pagina inicial,cambia pagina pero no la url
    lista = paginator.get_page(pagina)
    pagina_actual = int (pagina) #castear, utilizar con un formato en especial 
    paginas = range(1, lista.paginator.num_pages+1)
    return render(request, "servicio.html", {'servicios':lista,'paginas': paginas,'pagina_actual':pagina_actual})

#def tienda (request):
    #return render(request, "tienda.html", {})

# def blog (request):
#     return render(request, "blog.html", {})

# Esto es el fracmento de codigopara el vio de correo para el correo para contacto
#-------------------------------------------------------------------------------------------------------------------
# def contacto (request):
#     if request.method == 'POST':
#         subject = request.POST['asunto']
#         message =request.POST['nombre'] + request.POST['mensaje'] +' '+ 'del correo:' +' '+ request.POST['email']
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = ['web.kmx3@gmail.com']
#         send_mail(subject,  message,  email_from, recipient_list)
#         return HttpResponse("<h1> Gracias por enviar <h1>")
#     return render(request, "contacto.html", {})
#---------------------------------------------------------------------------------------------------------------------

def contacto(request):
    formulario= FormularioContacto()#creo variable formulario que me contendra todos los valores del fromulario creado en forms.py
    if request.method == 'POST':#evaluo si el metodo es post, verificable en el contacto.html
        formulario= FormularioContacto(data = request.POST)# captura los datos que estan dentro del formulario 
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            email=EmailMessage("App Gestion de Pedidos KMX",
                               "El usuario{} con Email {} Envió el siguiente asunto \n\n{}".format(nombre,email,contenido),
                               "",["web.kmx3@gmail.com"],reply_to=[email]) #reply es enviar las comillas solas son desde dindenme las envia
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?invalido')
                
            #return redirect('/contacto/?valido')
    return render(request, 'contacto.html', {'miformulario': formulario})

def mostrarcontacto (request):
    lista=Contacto.objects.all()
    return render (request,"mostrar_contacto.html",{'contacto':lista})
    

