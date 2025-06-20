from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = 'order'

urlpatterns = [
    path('create/', views.create_repair_order, name='create-order'),
    path('status/<str:order_number>/', views.get_order_status, name='order-status'),
    path('manage/<str:order_number>/', views.manage_order_details, name='manage-order'),
    path('', views.index),
] 
