from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar el inventario de productos.
    Provee automáticamente las operaciones CRUD.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer