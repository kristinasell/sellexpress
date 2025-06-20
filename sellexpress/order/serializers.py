from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import RepairOrder


class RepairOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = '__all__'
        read_only_fields = ('order_number', 'created_at', 'status')


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

class ManagerOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = [
            'job_titles',
            'main_jobs',
            'additional_jobs',
            'before_photos',
            'job_period_start',
            'job_period_end',
            'completed_jobs',
            'job_total_cost',
            'invoice_info',
            'payment_status',
            'after_photos',
            'estimated_cost',
            'estimated_completion',
            'status'
        ]
