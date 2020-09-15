# Generated by Django 3.1 on 2020-08-26 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20200826_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='country',
        ),
        migrations.AddField(
            model_name='shopuserprofile',
            name='lang',
            field=models.CharField(blank=True, max_length=32, verbose_name='язык страницы пользователя в ВК'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 28, 21, 51, 50, 2937)),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='vk_url',
            field=models.CharField(blank=True, max_length=32, verbose_name='страница в ВК'),
        ),
    ]