# Generated by Django 3.1 on 2020-09-02 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0018_auto_20200903_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 5, 1, 9, 54, 229037)),
        ),
    ]
