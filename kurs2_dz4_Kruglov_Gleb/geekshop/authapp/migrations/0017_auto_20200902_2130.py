# Generated by Django 3.1 on 2020-09-02 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_auto_20200902_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 4, 21, 30, 13, 361977)),
        ),
    ]
