from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('edicionProducto/<nombre>/', views.edicionProducto, name='edicionProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<nombre>/', views.eliminarProducto, name='eliminarProducto'),
]
