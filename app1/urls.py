
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import prueba,mis_proyectos,mis_tareas,mi_vista,agregar_tarea2,agregar_proyecto,detalle_proyecto,vista_login

urlpatterns = [
    path('',prueba),
    path('proyecto/',mis_proyectos),
    path('tareas/',mis_tareas),
    path('mi/',mi_vista),
    path('tareanueva/',agregar_tarea2),
    path('proyectonuevo',agregar_proyecto),
    path('detalle/<int:id>',detalle_proyecto,name='proyecto_tarea'),
    path('login/',vista_login,name='login'),
    path('cerrarseccion', LogoutView.as_view(template_name='cerrarseccion.html'), name='cerrarseccion'),

]
