
from django.urls import path
from .views import prueba,mis_proyectos,mis_tareas,mi_vista

urlpatterns = [
    path('',prueba),
    path('proyecto/',mis_proyectos),
    path('tareas/',mis_tareas),
    path('mi/',mi_vista)
]
