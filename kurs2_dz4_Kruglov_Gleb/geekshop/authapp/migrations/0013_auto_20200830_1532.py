# Generated by Django 3.1 on 2020-08-30 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20200826_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 15, 32, 23, 184403)),
        ),
    ]