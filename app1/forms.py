
from django import forms

class TareaNueva(forms.Form):
    titulo=forms.CharField(label='Nombre de tarea',max_length=50)
    descripcion=forms.CharField(widget=forms.Textarea)
    asociado=forms.CharField(label='De que proyecto?',max_length=50)

class Proyectonuevo(forms.Form):
    nombre=forms.CharField()
    fecha=forms.TimeField()