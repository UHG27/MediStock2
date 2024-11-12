from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.lista_productos, name='lista_productos'),  # Ruta base para inventarios
=======
    path('', views.home, name='home'),
>>>>>>> 58c7db769ec4714c4889351fe9ed5067f438edb7
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('edicionProducto/<nombre>/', views.edicionProducto, name='edicionProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<nombre>/', views.eliminarProducto, name='eliminarProducto'),
<<<<<<< HEAD
    path('login/', views.loginView, name='login'),
]
=======
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
>>>>>>> 58c7db769ec4714c4889351fe9ed5067f438edb7
