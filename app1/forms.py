
from django import forms

class TareaNueva(forms.Form):
    titulo=forms.CharField(label='Nombre de tarea',max_length=50)
    descripcion=forms.CharField(widget=forms.Textarea)
    asociado=forms.CharField(label='De que proyecto?',max_length=50)

class Editartarea(forms.Form):
    titulo=forms.CharField()
    descripcion=forms.CharField()

class Proyectonuevo(forms.Form):
    nombre=forms.CharField()
    fecha=forms.DateField()



class Editarproyecto(forms.Form):
    nombrenuevo=forms.CharField()
    fechanuevo=forms.DateField()


#Creacion y edicion de usuarios

    

class Editarusuario(forms.Form):
    mail=forms.EmailField(label='Cambiar mail')
    clave1=forms.CharField(label='Nueva clave',widget=forms.PasswordInput)
    clave2=forms.CharField(label='Repetir clave',widget=forms.PasswordInput)