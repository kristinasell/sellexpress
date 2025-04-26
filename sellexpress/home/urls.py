from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('invert/', views.invert_zero_one),
    path('api/orders/create/', views.create_repair_order, name='create-order'),
    path('api/orders/status/<str:order_number>/', views.get_order_status, name='order-status'),
    path('', views.index),
] 