import os
import json
from django.core.management import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


def load_json(file_name):
    with open(os.path.join('mainapp/json', file_name + '.json')) as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):

        super_user = ShopUser.objects.create_superuser(
            'django',
            'django@geekbrains.local',
            'geekbrains',
            age=29
        )

        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

        categories = load_json('ProductCategory')
        cats_dict = {}

        for cat in categories:
            new_cat = ProductCategory(**cat)
            new_cat.save()
            cats_dict[cat['name']] = new_cat.id

        products = load_json('Product')

        for product in products:
            product['category'] = ProductCategory.objects.get(name=product['category'])
            # product['category_id'] = cats_dict[product['category']]
            new_prod = Product(**product)
            new_prod.save()




