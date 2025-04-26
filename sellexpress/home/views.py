from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RepairOrder
from .serializers import RepairOrderCreateSerializer, RepairOrderStatusSerializer

@api_view(['POST'])
def create_repair_order(request):
    serializer = RepairOrderCreateSerializer(data=request.data)
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
