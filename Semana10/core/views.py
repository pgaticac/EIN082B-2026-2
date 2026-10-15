from django.shortcuts import render
from .models import Carrera

def home(request):
    return render(request,'core/home.html')

def carreras(request):
    list_carreras = Carrera.objects.all().order_by('nombre')
    

    titulo = "Carreras de Informática en Sede Viña"

    data = {
        'carreras': list_carreras,
        'titulo': titulo,
    }
    return render(request,'core/carreras.html',data)
