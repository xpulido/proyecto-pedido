from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = 'nombre', max_length = 30, required  = True)
    email = forms.EmailField(label = 'Email', max_length = 30, required = True)
    contenido = forms.CharField(label = 'Contenido', widget=(forms.Textarea), required = True)