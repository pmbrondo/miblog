from django.shortcuts import render,get_object_or_404
from .models import Tareas,Proyectos
from .forms import TareaNueva,Proyectonuevo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render

def prueba(requets):
    return render(requets,"inicio.html")

def mis_proyectos(requets):
    milista=Proyectos.objects.all()
    milista2=Proyectos.objects.values('id','nombre')
    print(milista2)
    return render (requets,"proyecto.html",{'milista2':milista2})

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
    

def agregar_proyecto(requets):
    if requets.method=='GET':
        return render(requets,'nuevoproyecto.html',{'formulario':Proyectonuevo})
    else:
        nuevoproyecto = requets.POST['nombre']
        fecha = requets.POST['fecha']
        Proyectos.objects.create(nombre=nuevoproyecto,fechacreacion=fecha)
        return render(requets,'nuevoproyecto.html',{'formulario':Proyectonuevo,'proyecto creado':'exito'})
    

def detalle_proyecto(requets,id):
    p=Proyectos.objects.get(id=id)
    a=tarea=Tareas.objects.filter(asociado=id)
    return render (requets,'detalle.html',{'proyecto':p,'listado':a})

#Usuarios, login y accesos.

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def vista_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                print(f"Bienvenido, {username}")
                return render(request, "inicio.html", {"mensaje":{username}})
            else:
                print("Error, datos mal ingresados")
                return render(request, "inicio.html", {"mensaje": "Error, datos mal ingresados"})
        else:
            print("Error, formulario incorrecto")
            return render(request, "inicio.html", {"mensaje": "Error, formulario incorrecto"})
    
    form = AuthenticationForm()
    return render(request, "login.html", {"formulario": form})

