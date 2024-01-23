
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (prueba,mis_proyectos,mis_tareas,mi_vista,agregar_tarea2,agregar_proyecto,
                    detalle_proyecto,vista_login,registro_usuario,editar_proyecto,elimar_proyecto,editar_proyecto2,
                    cambio_tareas,elimar_tarea,editar_tareas,editar_usuario,ver_perfil,prueba,cambio_generado)


urlpatterns = [
    path('',prueba),
    path('proyecto/',mis_proyectos,name='proyecto'),
    path('tareas/',mis_tareas),
    path('mi/',mi_vista),
    path('tareanueva/<int:id>/',agregar_tarea2,name='tareanueva'),
    path('proyectonuevo',agregar_proyecto,name='nuevoproyecto'),
    path('detalle/<int:id>',detalle_proyecto,name='proyecto_tarea'),
    path('login/',vista_login,name='login'),
    path('cerrarseccion', LogoutView.as_view(template_name='cerrarseccion.html'), name='cerrarseccion'),
    path('registro',registro_usuario,name='registro'),
    path('editarproyecto',editar_proyecto,name='editarproyecto'),
    path('editarproyecto2/<int:id>/', editar_proyecto2, name='editarproyecto2'),
    path('eliminarproyecto/<int:id>/', elimar_proyecto, name='eliminarproyecto'),
    path('cambiotareas/<int:id>/',cambio_tareas,name='cambiotareas'),
    path('eliminartarea/<int:id>/', elimar_tarea, name='eliminartarea'),
    path('editartarea/<int:id>/', editar_tareas, name='editartarea'),
    path('editarusuario.html/', editar_usuario, name='editarusuario'),
    path('miperfil.html',ver_perfil,name='miperfil'),
    path('cambioprocesado.html',cambio_generado,name='cambio'),
]
