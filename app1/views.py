from django.shortcuts import render
from .models import Tareas,Proyectos

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render

def prueba(requets):
    return render(requets,"inicio.html")

def mis_proyectos(requets):
    milista=Proyectos.objects.all()
    return render (requets,"proyecto.html",{'milista':milista})

def mis_tareas(requets):
    pendientes=Tareas.objects.all()
    return render(requets,'mistareas.html',{'pendientes':pendientes})

def mi_vista(requets):
    return render(requets,'acercademi.html')