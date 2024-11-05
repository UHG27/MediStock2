from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth.forms import AuthenticationForm

def Home(request):
    return render(request, 'templates/base.html')

def lista_productos(request):  # Agrega esta función
    productos = Producto.objects.all()
    return render(request, "inventarios/product.html", {"productos": productos})

def registrarProducto(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['numStock']
    fecha_creacion = request.POST['txtFechaDeCreacion']

    producto = Producto.objects.create(
        nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, fecha_creacion=fecha_creacion)
    return redirect('/inventarios/')

def edicionProducto(request, nombre):
    producto = Producto.objects.get(nombre=nombre)
    return render(request, "inventarios/edicionProducto.html", {"producto": producto})

def editarProducto(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['numStock']
    fecha_creacion = request.POST['txtFechaDeCreacion']

    producto = Producto.objects.get(nombre=nombre)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.fecha_creacion = fecha_creacion
    producto.stock = stock

    producto.save()

    return redirect('/inventarios/')

def eliminarProducto(request, nombre):
    producto = Producto.objects.get(nombre=nombre)
    producto.delete()

    return redirect('/inventarios/')

def loginView(request):
    return render(request, 'login.html', {
        'form': AuthenticationForm()
    })
