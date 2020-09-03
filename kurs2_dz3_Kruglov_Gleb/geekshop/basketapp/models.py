from django.db import models
from mainapp.models import Product
from geekshop import settings


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.quantity, items)))

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, items)))
