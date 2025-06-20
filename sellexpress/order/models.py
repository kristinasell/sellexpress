from django.db import models
import uuid

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

    # Дополнительные поля для менеджера:
    job_titles = models.TextField(blank=True, null=True, verbose_name='Наименования работ')  # (None)
    main_jobs = models.TextField(blank=True, null=True, verbose_name='Основные работы')  # (None)
    additional_jobs = models.JSONField(default=list, verbose_name='Дополнительные работы (bool-метки)')  # ([])
    before_photos = models.ImageField(upload_to='repairs/before/', blank=True, null=True, verbose_name='Фото до выполнения работ')  # (None)
    job_period_start = models.DateField(blank=True, null=True, verbose_name='Начало выполнения работ')  # (None)
    job_period_end = models.DateField(blank=True, null=True, verbose_name='Окончание выполнения работ')  # (None)
    completed_jobs = models.TextField(blank=True, null=True, verbose_name='Выполненные работы')  # (None)
    job_total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Стоимость работ')  # (None)
    invoice_info = models.TextField(blank=True, null=True, verbose_name='Счет')  # (None)
    payment_status = models.BooleanField(default=False, verbose_name='Статус оплаты')  # (False)
    after_photos = models.ImageField(upload_to='repairs/after/', blank=True, null=True, verbose_name='Фото после выполнения работ')  # (None)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = str(uuid.uuid4().int)[:10].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ №{self.order_number} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Заказ на ремонт'
        verbose_name_plural = 'Заказы на ремонт'



