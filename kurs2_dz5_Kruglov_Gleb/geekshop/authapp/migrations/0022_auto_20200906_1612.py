# Generated by Django 3.1 on 2020-09-06 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0021_auto_20200903_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 16, 12, 47, 442913)),
        ),
    ]
