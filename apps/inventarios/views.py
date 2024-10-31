

import requests
from django.shortcuts import render, redirect
from .models import Producto
from django.shortcuts import render, redirect
from .models import Producto



import requests
from django.shortcuts import render, redirect
from .models import Producto


def home(request):
    productos = Producto.objects.all()
    return render(request, "product.html", {"productos": productos})

def registrarProducto(request):



    # Obtener los datos del formulario
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['numStock']
    
    fecha_creacion = request.POST['txtFechaDeCreacion']

    # Crear el nuevo producto
    producto = Producto.objects.create(
        nombre=nombre, 
        descripcion=descripcion, 
        precio=precio, 
        stock=stock, 
        fecha_creacion=fecha_creacion
    )
    
    # Enviar datos a Zapier mediante Webhook
    webhook_url = 'https://hooks.zapier.com/hooks/catch/20484844/21jmlns/'
    data = {
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
        'stock': producto.stock,
        'fecha_creacion': producto.fecha_creacion.strftime("%Y-%m-%d")  # Convertir a cadena
    }
    
    print("Datos enviados a Zapier:", data)  # Imprime los datos que se envían

    # Realizar la solicitud POST a Zapier
    response = requests.post(webhook_url, json=data)

    # Verificar la respuesta del webhook
    if response.status_code == 200:
        print("Webhook enviado con éxito a Zapier.")
    else:
        print("Error al enviar el webhook a Zapier.", response.status_code, response.text)

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

    return render(request, "edicionProducto.html", {"nombre": nombre})

def editarProducto(request):
    # Obtener los datos del formulario
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['numStock']
    
    # Asegúrate de que 'txtFechaDeCreacion' es un campo de fecha
    fecha_creacion = request.POST['txtFechaDeCreacion']

    # Obtener el producto existente por nombre
    producto = Producto.objects.get(nombre=nombre)

    # Actualizar los datos del producto

    return render(request, "edicionProducto.html", {"nombre":nombre})

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


    productos = Producto.objects.filter(nombre=nombre)
    if productos.exists():
        productos.delete()  # Eliminar todos los productos con el nombre dado

    producto = Producto.objects.get(nombre=nombre)
    producto.delete()


    productos = Producto.objects.filter(nombre=nombre)
    if productos.exists():
        productos.delete()  # Eliminar todos los productos con el nombre dado

    return redirect('/')