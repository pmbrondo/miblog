from django.http import HttpResponse
from django.shortcuts import render

def prueba(requets):
    return render(requets,"inicio.html")
