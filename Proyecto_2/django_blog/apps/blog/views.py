from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def generales(request):
    return render(request,'generales.html')

def programacion(request):
    return render(request,'programacion.html')

def tutoriales(request):
    return render(request,'tutoriales.html')

def tecnologia(request):
    return render(request,'tecnologia.html')

def videojuegos(request):
    return render(request,'videojuegos.html')