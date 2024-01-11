from django.db import models

# Create your models here.

class Proyectos(models.Model):
    nombre=models.CharField(max_length=100)
    fechacreacion=models.DateField()



class Tareas(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()
    asociado=models.ForeignKey(Proyectos,on_delete=models.CASCADE)
