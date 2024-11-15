from django.shortcuts import render, redirect
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, "inventarios/product.html", {"productos": productos})

def registrarProducto(request):
    nombre=request.POST['txtNombre']
    descripcion=request.POST['txtDescripcion']
    precio=request.POST['txtPrecio']
    stock=request.POST['numStock']
    fecha_creacion=request.POST['txtFechaDeCreacion']

    producto = Producto.objects.create(
        nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, fecha_creacion=fecha_creacion)
    return redirect('/')

def edicionProducto(request, nombre):
    producto = Producto.objects.get(nombre=nombre)
    return render(request, "inventarios/edicionProducto.html", {"nombre":nombre})

def editarProducto(request):
    nombre=request.POST['txtNombre']
    descripcion=request.POST['txtDescripcion']
    precio=request.POST['txtPrecio']
    stock=request.POST['numStock']
    fecha_creacion=request.POST['txtFechaDeCreacion']

    producto = Producto.objects.get(nombre=nombre)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.fecha_creacion = fecha_creacion
    producto.stock = stock

    producto.save()

    return redirect('/')

def eliminarProducto(request, nombre):
    producto = Producto.objects.get(nombre=nombre)
    producto.delete()

    return redirect('/')