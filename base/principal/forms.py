from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Productor
from django.contrib.auth.forms import AuthenticationForm

class UsuarioCreationForm(UserCreationForm):
    primer_nombre = forms.CharField(max_length=100)
    segundo_nombre = forms.CharField(max_length=100)
    primer_apellido = forms.CharField(max_length=100)
    segundo_apellido = forms.CharField(max_length=100)
    correo = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('primer_nombre', 'segundo_nombre', 'primer_apellido', 
                    'segundo_apellido', 'correo', 'telefono', 'direccion', 'ciudad')

class ProductorCreationForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = '__all__'

class ProductorLoginForm(AuthenticationForm):
    pass

class UsuarioLoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ('correo', 'password')