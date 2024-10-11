from django.urls import path
from . import views

app_name = 'inventarios'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<str:sku>/', views.product_detail, name='product_detail'),
]