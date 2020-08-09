from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст')
