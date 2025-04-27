import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class RepairOrder(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('diagnostics', 'Диагностика'),
        ('repair', 'В ремонте'),
        ('waiting_parts', 'Ожидание запчастей'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    
    order_number = models.CharField(max_length=10, unique=True, editable=False)
    customer_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')
    equipment_type = models.CharField(max_length=100, verbose_name='Тип техники')
    model = models.CharField(max_length=100, blank=True, verbose_name='Модель')
    serial_number = models.CharField(max_length=50, blank=True, verbose_name='Серийный номер')
    problem_description = models.TextField(verbose_name='Описание проблемы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new',
        verbose_name='Статус'
    )
    estimated_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        verbose_name='Предварительная стоимость'
    )
    estimated_completion = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Предполагаемая дата завершения'
    )

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Генерируем номер заказа при создании
            self.order_number = str(uuid.uuid4().int)[:10].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ №{self.order_number} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Заказ на ремонт'
        verbose_name_plural = 'Заказы на ремонт'


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    is_mechanic = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return f"{self.username} ({self.email})"
