from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventarios/product_list.html', {'products': products})

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    return render(request, 'inventorios/product_detail.html', {'product': product})