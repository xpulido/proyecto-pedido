from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # creacion del usuario y ya creado el usuario  hacer la autenticacion 
from django.contrib.auth import login , logout , authenticate # hacer el logeo de la 
from django.contrib import messages 
from .forms import UserCreationFormWithEmail
#def autenticacion(request):
    #return render(request,'registro.html')

class VRegistro(View): # iniacializacion de una clase para el registro
    def get(self,request): #metodo paraget
        form = UserCreationFormWithEmail # es la variable que permite la creacion de formularios
        return render(request,'registro.html', {'form':form})# retorna el archivo renderizado de registro.html y el formulario de sus campos

    def post(self,request):
        form = UserCreationFormWithEmail(request.POST)
        usuario = form.save()
        if form.is_valid():
            login (request,usuario)
            messages.success(request, "usuario registrado")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, "registro.html",{"form":form})
    
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def Logear(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data = request.POST)#permite capturar los datos en el formulario de logeo
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contrasena)
            if usuario is not None: # si no esta el usuario,campo vacio
                login(request,usuario) #mande la peticion que yo envio el usuario y la contraseña
                return redirect('home')
            else:
                messages.error(request, 'Usuario no logeado')
        else:
            messages.error(request,'Informacion Incorrecta')
    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})
