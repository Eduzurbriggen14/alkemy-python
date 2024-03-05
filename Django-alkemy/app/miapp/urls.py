from django.urls import path
from .views import hola

urlpatterns = [
    path('', hola, name='hola'),
    # Puedes agregar más patrones de URL aquí
]