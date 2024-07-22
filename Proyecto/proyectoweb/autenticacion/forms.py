from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='requiere el correo', widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Direcion de correo'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Incluye el campo de correo electrónico

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail,self).save(commit=False)
        user.email = self.cleaned_data['email']  # Asigna el valor del campo de correo electrónico
        if commit:
            user.save()
        return user
