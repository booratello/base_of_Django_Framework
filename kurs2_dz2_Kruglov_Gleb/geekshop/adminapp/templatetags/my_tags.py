from django import template
from django.conf import settings

register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'products_images/default.jpg'
    return settings.MEDIA_URL + str(string)


register.filter('media_folder_products', media_folder_products)


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'avatars/default.jpg'
    return settings.MEDIA_URL + str(string)
