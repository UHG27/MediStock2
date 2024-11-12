from django.shortcuts import render

# Create your views here.
def reportes_home(request):
    return render(request, 'reportes/reportes.html')