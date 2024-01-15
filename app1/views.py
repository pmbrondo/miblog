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
    #print(milista2)
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
        #print(titulo)
        descripcion = requets.POST['descripcion']
        #print(descripcion)
        proyecto_id = requets.POST['asociado']
        #print(proyecto_id)
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
    #proyecto=Proyectos.objects.all()
    proyecto=Proyectos.objects.values('id','nombre')
    return render (request,'editarproyectos.html',{'proyecto':proyecto})

#segunda vista de edicion


def editar_proyecto2(request, id):
    print("Entré en la vista")
    proyecto = Proyectos.objects.get(id=id)

    if request.method == 'POST':
        print("Es un POST")
        formulario = Proyectonuevo(request.POST)
        if formulario.is_valid():
            print("El formulario es válido")
            datos = formulario.cleaned_data
            proyecto.nombre = datos['nombre']
            proyecto.fechacreacion = datos['fecha']
            proyecto.save()
            print("Guardé el proyecto")
            return render(request, 'inicio.html')
        else:
            print("El formulario no es válido")
    else:
        print("No es un POST")
        formulario = Proyectonuevo(initial={'nombre': proyecto.nombre, 'fecha': proyecto.fechacreacion})

    print("Antes de renderizar")
    return render(request, 'editarproyecto2.html', {'proyecto': proyecto, 'formulario': formulario})


    # Resto del código si es un GET o si el formulario no es válido

    #else:
   #     formulario = Proyectonuevo(initial={'nombre': proyecto.nombre, 'fecha': proyecto.fechacreacion})
    #return render(request, 'editarproyecto2.html',{'formulario': formulario, 'proyecto': proyecto})
   

#def editar_proyecto3(request):
#   proyecto=Proyectos.objects.get()
 #   print(proyecto)

 #   if request.method == 'POST':
  #      pass
        #proyecto = get_object_or_404(Proyectos, nombre=a)
        #formulario=request.POST
        #print(formulario)
        #a=formulario['nombre']
        #b=formulario['fecha']
        #print("llego")
        #proyecto = get_object_or_404(Proyectos, nombre=a)
        #print(proyecto)
        #print("hola")
        #proyecto.nombre=a
        #proyecto.fechacreacion=b
        #proyecto.save()
        #print(c)
        #formulario.save()
    #formulario=Proyectonuevo (initial={"nombre":proyecto.nombre,"fecha":proyecto.fechacreacion})
    #return render(request, 'editarproyecto3.html',{"formulario":formulario})  # Ajusta esto a tu nombre de vista de inicio

    #else:
    #   formulario = Proyectonuevo()

    #return render(request, 'editarproyecto3.html', {'formulario': formulario})


        







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