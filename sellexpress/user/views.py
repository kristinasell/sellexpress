from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from order.serializers import RepairOrderSerializer
from order.models import RepairOrder


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'username': user.username
        })

class UserOrdersAPIView(generics.ListAPIView):
    serializer_class = RepairOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RepairOrder.objects.filter(
            phone_number=self.request.user.phone
        ).order_by('-created_at')

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
