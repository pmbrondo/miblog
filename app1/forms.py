
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TareaNueva(forms.Form):
    titulo=forms.CharField(label='Nombre de tarea',max_length=50)
    descripcion=forms.CharField(widget=forms.Textarea)
    asociado=forms.CharField(label='De que proyecto?',max_length=50)

class Editartarea(forms.Form):
    titulo=forms.CharField()
    descripcion=forms.CharField()
    estado=forms.BooleanField()

class Proyectonuevo(forms.Form):
    nombre=forms.CharField()
    fecha=forms.DateField()



class Editarproyecto(forms.Form):
    nombrenuevo=forms.CharField()
    fechanuevo=forms.DateField()


#Creacion y edicion de usuarios

class Crearusuario(UserCreationForm):
    email = forms.EmailField(label='Ingresa tu email: ')
    password1 = forms.CharField(label="Contraseña: ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña: ", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}



class Editarusuario(UserCreationForm):
    usuario=forms.CharField(label='Cambiar usuario')
    password1=forms.CharField(label='Nueva clave',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir clave',widget=forms.PasswordInput)
    email=forms.EmailField(label=' Cambiar email')
    last_name=forms.CharField(label='Cambiar Apellido')
    first_name=forms.CharField(label='Cambiar Nombre')

    class Meta:
        model= User
        fields = ['usuario', 'password1', 'password2','email', 'last_name', 'first_name']
        help_texts={k:"" for k in fields}