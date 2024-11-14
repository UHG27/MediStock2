from django.shortcuts import render
from django.http import HttpResponse
from apps.inventarios.models import Producto
from apps.ventas.models import Venta
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from datetime import datetime
import os

def reportes(request):
    # Obtén los datos de inventario y ventas
    productos = Producto.objects.all()
    ventas = Venta.objects.all()

    # Calcula la cantidad restante de cada producto y registra la fecha de cada venta
    reporte_datos = []
    for producto in productos:
        total_vendido = 0
        fechas_ventas = []
        for venta in ventas:
            if venta.producto == producto:
                total_vendido += venta.cantidad
                fechas_ventas.append(venta.fecha.strftime("%d/%m/%Y"))  # Formato de fecha DD/MM/AAAA
        cantidad_restante = producto.stock - total_vendido
        reporte_datos.append({
            'nombre': producto.nombre,
            'cantidad_restante': cantidad_restante,
            'fechas_ventas': fechas_ventas,
        })

    # Generar PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_inventario.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle("Reporte de Inventario y Ventas")

    # Insertar logo
    logo_path = os.path.join('static', 'img', 'Genericos.png')  # Ruta del logo
    p.drawImage(logo_path, 40, 730, width=80, height=80)  # Ajusta la posición y tamaño del logo

    # Añadir título y fecha
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    p.drawString(150, 800, "Reporte de Inventario y Ventas")
    p.drawString(150, 780, f"Fecha: {fecha_actual}")

    # Preparar datos para la tabla
    encabezados = ["Producto", "Cantidad Restante", "Fechas de Ventas"]
    filas = [[
        item['nombre'], 
        item['cantidad_restante'], 
        ", ".join(item['fechas_ventas'])  # Une las fechas de ventas en una sola cadena
    ] for item in reporte_datos]
    data = [encabezados] + filas

    # Crear y estilizar la tabla
    tabla = Table(data, colWidths=[2.5 * inch, 1.5 * inch, 3 * inch])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Posicionar y dibujar la tabla en el PDF
    tabla.wrapOn(p, 300, 500)
    tabla.drawOn(p, 50, 550)

    # Finalizar el PDF
    p.showPage()
    p.save()

    return response
