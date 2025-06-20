from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import RepairOrder
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


@api_view(['POST'])
def create_repair_order(request):
    data = request.data.copy()
    if request.user.is_authenticated:
        data['phone_number'] = request.user.phone  # Автоматически подставляем телефон
    
    serializer = RepairOrderCreateSerializer(data=data)
    if serializer.is_valid():
        order = serializer.save()
        return Response({
            'status': 'success',
            'message': 'Заказ создан успешно',
            'order_number': order.order_number
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order_status(request, order_number):
    try:
        order = RepairOrder.objects.get(order_number=order_number)
        serializer = RepairOrderStatusSerializer(order)
        return Response(serializer.data)
    except RepairOrder.DoesNotExist:
        return Response(
            {'error': 'Заказ с таким номером не найден'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['PUT'])
@permission_classes([IsAuthenticated])  # только авторизованные
def manage_order_details(request, order_number):
    try:
        order = RepairOrder.objects.get(order_number=order_number)
    except RepairOrder.DoesNotExist:
        return Response({'error': 'Заказ не найден'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ManagerOrderUpdateSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Информация по заказу успешно обновлена'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Главная страница
def index(request):    
    return HttpResponse('Sellexpress')

def invert_zero_one(request):
    # Получаем значение из GET-параметра 'value'
    input_value = request.GET.get('value', '').strip()
    
    if input_value == '0':
        response = '1'
    elif input_value == '1':
        response = '0'
    else:
        response = 'Только 0 или 1!'
    
    return JsonResponse({'result': response})


