# Generated by Django 3.1 on 2020-09-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_auto_20200909_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активен'),
        ),
    ]