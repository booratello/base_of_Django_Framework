# Generated by Django 3.1 on 2020-09-16 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0022_auto_20200906_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 20, 39, 17, 977792)),
        ),
    ]
