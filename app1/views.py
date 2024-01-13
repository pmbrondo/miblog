from django.shortcuts import render,get_object_or_404
from .models import Tareas,Proyectos
from .forms import TareaNueva,Proyectonuevo,Editarproyecto
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.





def prueba(requets):
    return render(requets,"inicio.html")

@login_required
def mis_proyectos(requets):
    milista=Proyectos.objects.all()
    milista2=Proyectos.objects.values('id','nombre')
    print(milista2)
    return render (requets,"proyecto.html",{'milista2':milista2})

@login_required
def mis_tareas(requets):
    pendientes=Tareas.objects.all()
    return render(requets,'mistareas.html',{'pendientes':pendientes})


def mi_vista(requets):
    return render(requets,'acercademi.html')


@login_required
def agregar_tarea(requets):
    titulo = requets.GET.get('titulo')
    descripcion = requets.GET.get('descripcion')
    proyecto_id = requets.GET.get('asociado')
    proyecto = get_object_or_404(Proyectos, nombre=proyecto_id)
    #Tareas.objects.create(titulo=requets.GET['titulo'],descripcion=requets.GET['descripcion'],asociado=requets.GET['asociado'])
    Tareas.objects.create(titulo=titulo, descripcion=descripcion, asociado=proyecto)
    #return render(requets,'tareanueva.html',{'formulario':TareaNueva})
    return render(requets, 'tareanueva.html', {'formulario': TareaNueva, 'exito': 'Tarea creada con éxito'})

@login_required
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
    
@login_required
def agregar_proyecto(requets):
    if requets.method=='GET':
        return render(requets,'nuevoproyecto.html',{'formulario':Proyectonuevo})
    else:
        nuevoproyecto = requets.POST['nombre']
        fecha = requets.POST['fecha']
        Proyectos.objects.create(nombre=nuevoproyecto,fechacreacion=fecha)
        return render(requets,'nuevoproyecto.html',{'formulario':Proyectonuevo,'proyecto creado':'exito'})



# tengo que cambiar la logica porque es para registar no para editar
def editar_proyecto(request):
    if request.method=='GET':
        return render(request,'editarproyectos.html',{'formulario':Editarproyecto})
    else:
        n = request.POST['nombrenuevo']
        f = request.POST['fechanuevo']
        Proyectos.objects.create(nombre=n,fechacreacion=f)
        return render(request,'editarproyectos.html',{'formulario':Editarproyecto,'proyecto editado':'exito'})

#revisar proque necesito 2 argumentos y no consigo enviarlos
def elimar_proyecto(request,nombre_borrar):
    proyecto=Proyectos.objects.get(nombre=nombre_borrar)
    print(proyecto)
    proyecto.delete()

    proyecto=Proyectos.objects.all()
    return render (request,'proyecto.html',{'proyecto':proyecto})
    
@login_required
def detalle_proyecto(requets,id):
    p=Proyectos.objects.get(id=id)
    a=tarea=Tareas.objects.filter(asociado=id)
    return render (requets,'detalle.html',{'proyecto':p,'listado':a})

#Usuarios, login y accesos.





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


def registro_usuario(requests):

    if requests.method=='POST':
        formulario=UserCreationForm(requests.POST)
        if formulario.is_valid():
            usermane=formulario.cleaned_data['username']
            formulario.save()
            print('usuario creado')
            return render(requests,"inicio.html",{'mesaje':'usuario creado'})
    else:
        formulario=UserCreationForm()
    return render(requests,"registro.html",{"formulario":formulario})