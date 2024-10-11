from django.shortcuts import render
# from .models import ventas

# Create your views here.
def ventas(request):
    ventas = Sale.objects.all()
    return render(request, 'templates/ventas/ventas.html', {'sales': sales}) 