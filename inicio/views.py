from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# VISTA UNO
#def inicio(request):
#    return HttpResponse('Esta es tu primera vista de inicio')

def inicio(request):
    return render(request, "inicio/inicio.html", {})

def productos(request):
    return render(request, "inicio/productos.html", {})
