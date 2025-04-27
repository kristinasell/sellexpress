from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = 'home'

urlpatterns = [
    path('auth/register/', views.RegisterAPIView.as_view(), name='register'),
    path('auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.UserProfileAPIView.as_view(), name='profile'),
    path('my-orders/', views.UserOrdersAPIView.as_view(), name='user-orders'),
    path('invert/', views.invert_zero_one),
    path('api/orders/create/', views.create_repair_order, name='create-order'),
    path('api/orders/status/<str:order_number>/', views.get_order_status, name='order-status'),
    path('', views.index),
] 