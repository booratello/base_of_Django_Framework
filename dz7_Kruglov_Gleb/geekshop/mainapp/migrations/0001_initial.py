# Generated by Django 3.1rc1 on 2020-07-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название каегории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
        ),
    ]
