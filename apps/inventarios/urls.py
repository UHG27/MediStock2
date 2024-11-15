from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('edicionProducto/<str:nombre>/', views.edicionProducto, name='edicionProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<str:nombre>/', views.eliminarProducto, name='eliminarProducto'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
]
