from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # Ruta base para inventarios
    path('home/', views.home, name='home'),  # Ruta separada para 'home' si la necesitas
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('edicionProducto/<str:nombre>/', views.edicionProducto, name='edicionProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<str:nombre>/', views.eliminarProducto, name='eliminarProducto'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Solo una ruta para login
    path('logout/', LogoutView.as_view(), name='logout'),  # Solo una ruta para logout
]
