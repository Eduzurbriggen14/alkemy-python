from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto

# Create (Create a new product)
def producto_create(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')     

        producto = Producto.objects.create(
            nombreProducto=nombreProducto,
            descripcion=descripcion,
            categoria=categoria,
            precio=precio,
            cantidad=cantidad
        )
        return redirect('producto_list')
    else:
        return render(request, 'producto_form.html') 
    

def producto_list(request):
    productos = Producto.objects.all() 
    context = {'productos': productos}
    return render(request, 'producto_list.html', context)

def producto_update(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.nombreProducto = request.POST.get('nombreProducto')
        producto.descripcion = request.POST.get('descripcion')
        producto.categoria = request.POST.get('categoria')
        producto.precio = request.POST.get('precio')
        producto.cantidad = request.POST.get('cantidad')

        producto.save()  
        return redirect('producto_list')
    else:
        context = {'producto': producto}
        return render(request, 'producto_form.html', context)  
    
def producto_delete(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete() 
        return redirect('producto_list') 
    else:
        context = {'producto': producto}
        return render(request, 'producto_confirm_delete.html', context)