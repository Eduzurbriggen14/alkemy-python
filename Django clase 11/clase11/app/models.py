from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        ordering = ('nombreProducto',)
        
    def __str__(self):
        return self.nombreProducto