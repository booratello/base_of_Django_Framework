# Generated by Django 3.1 on 2020-09-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Товар активен'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Категория активна'),
        ),
    ]
