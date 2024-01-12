from django.shortcuts import render,get_object_or_404
from .models import Tareas,Proyectos
from .forms import TareaNueva

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

def agregar_tarea(requets):
    titulo = requets.GET.get('titulo')
    descripcion = requets.GET.get('descripcion')
    proyecto_id = requets.GET.get('asociado')
    proyecto = get_object_or_404(Proyectos, nombre=proyecto_id)
    #Tareas.objects.create(titulo=requets.GET['titulo'],descripcion=requets.GET['descripcion'],asociado=requets.GET['asociado'])
    Tareas.objects.create(titulo=titulo, descripcion=descripcion, asociado=proyecto)
    #return render(requets,'tareanueva.html',{'formulario':TareaNueva})
    return render(requets, 'tareanueva.html', {'formulario': TareaNueva, 'exito': 'Tarea creada con éxito'})


def agregar_tarea2(requets):
    if requets.method=='GET':
        return render(requets,'tareanueva.html',{'formulario':TareaNueva})
        
    else:
        titulo = requets.POST['titulo']
        print(titulo)
        descripcion = requets.POST['descripcion']
        print(descripcion)
        proyecto_id = requets.POST['asociado']
        print(proyecto_id)
        proyecto = get_object_or_404(Proyectos, nombre=proyecto_id)
    #Tareas.objects.create(titulo=requets.GET['titulo'],descripcion=requets.GET['descripcion'],asociado=requets.GET['asociado'])
        Tareas.objects.create(titulo=titulo, descripcion=descripcion, asociado=proyecto)
    #return render(requets,'tareanueva.html',{'formulario':TareaNueva})
        return render(requets, 'tareanueva.html', {'formulario': TareaNueva, 'exito': 'Tarea creada con éxito'})
        