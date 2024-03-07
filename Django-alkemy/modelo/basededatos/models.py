from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=15, blank=False)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()

    # metadatos
    class Meta:
        ordering = ['-nombre']

    # metodos/funciones del modelo
    def __str__(self) -> str:
        return self.nombre
