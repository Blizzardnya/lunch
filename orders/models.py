from django.db import models
from cafe.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    """Модель заказа"""
    customer = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    NEW = 'N'
    IN_PROCESS = 'P'
    COMPLETE = 'C'

    ORDER_STATUS = (
        (NEW, 'New'),
        (IN_PROCESS, 'In process'),
        (COMPLETE, 'Complete'),
    )

    status = models.CharField('Статус', max_length=1, choices=ORDER_STATUS, default=NEW)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return 'Order {}'.format(self.id)


class OrderItem(models.Model):
    """Модель строк заказа"""
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Строка заказа'
        verbose_name_plural = 'Строки заказа'

    def get_cost(self):
        return self.price * self.quantity
