
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (prueba,mis_proyectos,mis_tareas,mi_vista,agregar_tarea2,agregar_proyecto,
                    detalle_proyecto,vista_login,registro_usuario,editar_proyecto,elimar_proyecto,editar_proyecto2)
                    #editar_proyecto3)


urlpatterns = [
    path('',prueba),
    path('proyecto/',mis_proyectos),
    path('tareas/',mis_tareas),
    path('mi/',mi_vista),
    path('tareanueva/',agregar_tarea2),
    path('proyectonuevo',agregar_proyecto,name='nuevoproyecto'),
    path('detalle/<int:id>',detalle_proyecto,name='proyecto_tarea'),
    path('login/',vista_login,name='login'),
    path('cerrarseccion', LogoutView.as_view(template_name='cerrarseccion.html'), name='cerrarseccion'),
    path('registro',registro_usuario,name='registro'),
    path('editarproyecto',editar_proyecto,name='editarproyecto'),
    path('editarproyecto2/<int:id>/', editar_proyecto2, name='editarproyecto2'),
    path('eliminarproyecto/<int:id>/', elimar_proyecto, name='eliminarproyecto'),
]
