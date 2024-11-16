import requests
from django.shortcuts import render, redirect
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, "inventarios/product.html", {"productos": productos})

def registrarProducto(request):
<<<<<<< HEAD
    # Obtener los datos del formulario
=======
>>>>>>> 3cb040c048bae306feb8393a85a98a8a7327dc89
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['numStock']
<<<<<<< HEAD
    
=======
>>>>>>> 3cb040c048bae306feb8393a85a98a8a7327dc89
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

    return redirect('/')

def edicionProducto(request, nombre):
    producto = Producto.objects.get(nombre=nombre)
<<<<<<< HEAD
    return render(request, "edicionProducto.html", {"nombre": nombre})

def editarProducto(request):
    # Obtener los datos del formulario
=======
    return render(request, "inventarios/edicionProducto.html", {"producto": producto})

def editarProducto(request):
>>>>>>> 3cb040c048bae306feb8393a85a98a8a7327dc89
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    stock = request.POST['numStock']
<<<<<<< HEAD
    
    # Asegúrate de que 'txtFechaDeCreacion' es un campo de fecha
=======
>>>>>>> 3cb040c048bae306feb8393a85a98a8a7327dc89
    fecha_creacion = request.POST['txtFechaDeCreacion']

    # Obtener el producto existente por nombre
    producto = Producto.objects.get(nombre=nombre)

    # Actualizar los datos del producto
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
    return redirect('/')