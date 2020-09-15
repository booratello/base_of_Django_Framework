from django.db import models
from mainapp.models import Product
from geekshop import settings
from django.utils.functional import cached_property


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @cached_property
    def get_items_cached(self):
    	return self.user.basket.select_related()

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        # items = self.get_items_cached
        return sum(list(map(lambda x: x.quantity, items)))

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        # items = self.get_items_cached
        return sum(list(map(lambda x: x.product_cost, items)))

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()
