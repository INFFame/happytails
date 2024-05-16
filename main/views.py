from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def servicios(request):
    return render(request, "servicios.html")

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request):
    return render(request, "contacto.html")