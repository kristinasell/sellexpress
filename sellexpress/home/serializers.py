from rest_framework import serializers
from .models import RepairOrder

class RepairOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = [
            'customer_name', 
            'phone_number',
            'equipment_type',
            'model',
            'serial_number',
            'problem_description'
        ]

class RepairOrderStatusSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = RepairOrder
        fields = [
            'order_number',
            'status',
            'status_display',
            'estimated_cost',
            'estimated_completion',
            'created_at'
        ]
        read_only_fields = fields