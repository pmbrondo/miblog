from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Proyectos(models.Model):
    nombre=models.CharField(max_length=100)
    fechacreacion=models.DateField()

    def __str__(self) -> str:
        return self.nombre


class Tareas(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()
    asociado=models.ForeignKey(Proyectos,on_delete=models.CASCADE)
    estado= models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo


class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
