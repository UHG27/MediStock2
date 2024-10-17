from django.shortcuts import render
from .models import Producto


def home(request):
    productos = Producto.objects.all()
    return render(request, "product.html", {"productos": productos})
