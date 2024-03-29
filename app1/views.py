from django.shortcuts import render,get_object_or_404
from .models import Tareas,Proyectos,Avatar
from .forms import TareaNueva,Proyectonuevo,Editarproyecto,Editartarea,Editarusuario,Crearusuario,FormularioAvatar
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from itertools import groupby
from django.contrib.auth.models import User

# Create your views here.


#prueba avatar
def misavatares(request):
    if request.user.is_authenticated:
        a = request.user
        miavatar = Avatar.objects.filter(user=request.user).first()
      
        return render(request,"herencia.html",{'avatar': miavatar,'usuario':a})
    else:
        return render(request, "herencia.html")



#general
def prueba(requets):
    if requets.user.is_authenticated:
        miavatar = Avatar.objects.filter(user=requets.user).first()
        #'avatar': miavatar,
        a=requets.user
        return render(requets,"inicio.html",{'avatar': miavatar,'usuario':a})
    else:
        return render(requets,"inicio.html")

#mis datos 
def mi_vista(requets):
    return render(requets,'acercademi.html')

#Proyectos generados 
@login_required
def mis_proyectos(requets):
    milista=Proyectos.objects.all()
    milista2=Proyectos.objects.values('id','nombre')
    #print(milista2)
    return render (requets,"proyecto.html",{'milista2':milista2})


#Veo todas las tareas pendientes.
@login_required
def mis_tareas(requets):
    pendientes=Tareas.objects.values()
    
    pendientes2=Proyectos.objects.values()
    
    # Ordenar el QuerySet por 'asociado_id'
    tus_datos = sorted(pendientes, key=lambda x: x['asociado_id'])
    grupos = {k: list(g) for k, g in groupby(tus_datos, key=lambda x: x['asociado_id'])}
    mati = []
    for asociado_id, items in grupos.items():
        asociado_dict = {'asociado_id': asociado_id, 'tareas': []}
        for item in items:
            tarea_dict = {
                'id': item['id'],
                'titulo': item['titulo'],
                'descripcion': item['descripcion'],
                'estado': item['estado']
                }
            proyecto_id = item.get('proyecto_id')
            proyecto_info = next((p for p in pendientes2 if p['id'] == proyecto_id), None)

            if proyecto_info:
                tarea_dict['proyecto'] = {
                    'id': proyecto_info['id'],
                    'nombre': proyecto_info['nombre'],
                    'fechacreacion': proyecto_info['fechacreacion']
                }

            asociado_dict['tareas'].append(tarea_dict)

        mati.append(asociado_dict)
    return render(requets,'mistareas.html',{'pendientes':mati,'pendientes2':pendientes2})


def cambio_generado(requets):
    return render(requets,'cambioprocesado.html')


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
def agregar_tarea2(request,id):
    
    tarea = get_object_or_404(Proyectos, id=id)
    print(tarea)
    if request.method=='GET':
        print('Hello world2')
        #formulario = Editartarea(initial={'titulo': tarea.titulo, 'descripcion': tarea.descripcion,'estado':tarea.estado})
        formulario = TareaNueva(initial={'asociado': tarea})
        return render(request,'tareanueva.html',{'formulario':formulario})
        
    else:
        print('Hello world3')
        titulo = request.POST['titulo']
        #print(titulo)
        descripcion = request.POST['descripcion']
        #print(descripcion)
        proyecto_id = request.POST['asociado']
        #print(proyecto_id)
        proyecto = get_object_or_404(Proyectos, nombre=proyecto_id)
    #Tareas.objects.create(titulo=requets.GET['titulo'],descripcion=requets.GET['descripcion'],asociado=requets.GET['asociado'])
        Tareas.objects.create(titulo=titulo, descripcion=descripcion, asociado=proyecto)
    #return render(requets,'tareanueva.html',{'formulario':TareaNueva})
        return render(request, 'cambioprocesado.html', {'formulario': TareaNueva, 'exito': 'Tarea creada con éxito','proyecto':proyecto})
        
    


#Editar tareas  
def cambio_tareas(request,id):
    print('Hola')
    proyecto = get_object_or_404(Proyectos, id=id)
    tareas_asociadas = Tareas.objects.filter(asociado=proyecto)
    context = {
        'proyecto': proyecto,
        'tareas_asociadas': tareas_asociadas,
    }

    return render(request, 'cambiotareas.html', context)

@login_required
def editar_tareas(request,id):
    print("Entré en la vista")
    tarea = Tareas.objects.get(id=id)
    
    if request.method == 'POST':
        print("Es un POST")
        formulario = Editartarea(request.POST)
        if formulario.is_valid():
            print("El formulario es válido")
            datos = formulario.cleaned_data
            tarea.titulo = datos['titulo']
            tarea.descripcion = datos['descripcion']
            tarea.estado=datos['estado']
            tarea.save()
            print("Guardé el proyecto")
            return render(request, 'tareaeditada.html')
        else:
            print("El formulario no es válido")
    else:
        print("No es un POST")
        formulario = Editartarea(initial={'titulo': tarea.titulo, 'descripcion': tarea.descripcion,'estado':tarea.estado})

    print("Antes de renderizar")
    return render(request, 'editartarea.html', {'tarea': tarea, 'formulario': formulario})

#Eliminar tareas
@login_required
def elimar_tarea(request,id):
    tarea=Tareas.objects.get(id=id)
    print(tarea)
    tarea.delete()
    tarea=Proyectos.objects.all()
    return render(request, 'elimarproyecto.html', {'tarea': tarea})








@login_required
def agregar_proyecto(requets):
    if requets.method=='GET':
        return render(requets,'nuevoproyecto.html',{'formulario':Proyectonuevo})
    else:
        nuevoproyecto = requets.POST['nombre']
        fecha = requets.POST['fecha']
        Proyectos.objects.create(nombre=nuevoproyecto,fechacreacion=fecha)
        return render(requets,'cambioprocesado.html',{'formulario':Proyectonuevo,'proyecto creado':'exito'})



# tengo que cambiar la logica porque es para registar no para editar
@login_required
def editar_proyecto(request):
    #proyecto=Proyectos.objects.all()
    proyecto=Proyectos.objects.values('id','nombre')
    return render (request,'editarproyectos.html',{'proyecto':proyecto})

#segunda vista de edicion

@login_required
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


#revisar proque necesito 2 argumentos y no consigo enviarlos
@login_required
def elimar_proyecto(request,id):
    proyecto=Proyectos.objects.get(id=id)
    print(proyecto)
    proyecto.delete()
    proyectos=Proyectos.objects.all()
    return render(request, 'elimarproyecto.html', {'proyectos': proyectos})

    #return render (request,'eliminarproyecto',{'proyecto':proyecto})



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
                #print(f"Bienvenido, {username}")
                #Pruebo enviar solo el nombre de usuario para evitar el for!
                #pruebo enviar a herencia
                #, {"mensaje":username}
                miavatar = Avatar.objects.filter(user=request.user).first()
                a=request.user
                print(a)
                return render(request, "inicio.html",{'avatar': miavatar,'usuario':a})
    
            else:
                print("Error, datos mal ingresados")
                return render(request, "inicio.html", {"mensaje": "Error, datos mal ingresados"})
        else:
            print("Error, tus datos son incorrectos")
            return render(request, "inicio.html", {"mensaje": "Error, formulario incorrecto"})
    
    form = AuthenticationForm()
    return render(request, "login.html", {"formulario": form})

#Crear usuarios

def registro_usuario(request):

    if request.method=='POST':
        formulario=Crearusuario(request.POST)
        if formulario.is_valid():
            usermane=formulario.cleaned_data['username']
            print(usermane)
            formulario.save()
            print('usuario creado')
            #login (requests, formulario)
            return render(request,"inicio.html",{'mesaje':'usuario creado'})
    else:
        formulario=Crearusuario()
    return render(request,"registro.html",{"formulario":formulario})



#edito mi usuario

@login_required
def editar_usuario(request):
   
    usuario = request.user

    if request.method == 'POST':

        miFormulario = Editarusuario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.usuario = informacion['usuario']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = Editarusuario()

    return render(request, "editarusuario.html", {"miFormulario": miFormulario, "usuario": usuario})

#Ver mi perfil

    
@login_required
def ver_perfil(request):
    usuario = request.user
    print(usuario)
    usuarios = User.objects.values()
    print(usuarios)
    lista_usuarios = [dict(usuario) for usuario in usuarios]
    miavatar = Avatar.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = FormularioAvatar(request.POST, request.FILES, instance=miavatar)
        if form.is_valid():
            miavatar = form.save(commit=False) 
            miavatar.user = request.user  
            miavatar.save()  
            return redirect('miperfil')
    else:
        form = FormularioAvatar(instance=miavatar)

    return render(request, 'miperfil.html', {'usuarios': lista_usuarios, 'usuario': usuario, 'avatar': miavatar, 'form': form})
