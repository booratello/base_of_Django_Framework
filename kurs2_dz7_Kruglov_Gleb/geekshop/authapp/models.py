import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(datetime.now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activation_key_expires:
            return True
        else:
            return False


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    UNDEFINED = 'U'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
        (UNDEFINED, ''),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=128, blank=True, verbose_name='теги')
    aboutMe = models.TextField(blank=True, verbose_name='о себе')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, verbose_name='пол')
    vk_url = models.CharField(max_length=32, blank=True, verbose_name='страница в ВК')
    lang = models.CharField(max_length=32, blank=True, verbose_name='язык страницы пользователя в ВК')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
