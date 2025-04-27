from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, RepairOrder


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            phone=validated_data['phone']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные данные")


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