from django.shortcuts import render
from .models import Usuario

def crear_usuario(request):
    usuario = Usuario.objects.create(
        nombre="Eduardo",
        apellido="Zurbriggen",
        dni=12345678,
        edad=236
    )

    usuario2 = Usuario.objects.create(
        nombre="Nicolas",
        apellido="Garcia",
        dni=1231236,
        edad=36
    )

    return render(request, 'usuario.html', {'usuarios': [usuario, usuario2]})
