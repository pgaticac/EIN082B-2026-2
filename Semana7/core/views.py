from django.shortcuts import render, HttpResponse

def home(request):
    mensaje = "<h1>Hola Mundo</h1>"
    
    #return HttpResponse(mensaje)
    return render(request,'core/home.html')

def uno(request):
    return render(request, 'core/uno.html')
def dos(request):
    return render(request, 'core/dos.html')
def tres(request):
    return render(request, 'core/tres.html')