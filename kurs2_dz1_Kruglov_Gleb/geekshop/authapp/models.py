import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(datetime.now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activation_key_expires:
            return True
        else:
            return False
