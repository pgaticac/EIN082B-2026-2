from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def carreras(request):
    list_carreras = list()
    list_carreras.append("Ingeniería en Informática")
    list_carreras.append("Técnico Universitario en Informática")
    list_carreras.append("Ingeniería de Ejecución en Software")
    list_carreras.append("Ingeniería Civil Informática")

    titulo = "Carreras de Informática en Sede Viña"

    data = {
        'carreras': list_carreras,
        'titulo': titulo,
    }
    return render(request,'core/carreras.html',data)
