from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("<h1>Hola a todos</h1>")

# Create your views here.