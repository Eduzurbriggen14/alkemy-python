from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def estudiante(request):
    estudiante_curso = [
        {"nombre": "nicolas", "cursos": [{"titulo": "React", "descripcion": "Framework de Js"}, 
                                         {"titulo": "Python", "descripcion": "Lenguaje"}]},

        {"nombre": "carlos", "cursos": []},
        
        {"nombre": "agostina", "cursos": [{"titulo": "Python", "descripcion": "Lenguaje"},
                                          {"titulo": "Django", "descripcion": "Framework de Python"}]}
    ]

    ruta = "C:/Users/Gorila Games/Desktop/alkemy-python/Django-clase12/clase12/app/templates/index.html"
    archivo = open(ruta)
    contenido = archivo.read()
    template = Template(contenido)
    archivo.close()
    context = Context({"estudiantes": estudiante_curso})

    return HttpResponse(template.render(context))
