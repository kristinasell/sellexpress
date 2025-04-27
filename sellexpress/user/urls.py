from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = 'user'

urlpatterns = [
    path('auth/register/', views.RegisterAPIView.as_view(), name='register'),
    path('auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.UserProfileAPIView.as_view(), name='profile'),
    path('my-orders/', views.UserOrdersAPIView.as_view(), name='user-orders'),
] 