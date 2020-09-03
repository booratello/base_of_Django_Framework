from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile
from PIL import Image
from io import BytesIO


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about',
                                                                 'domain', 'photo_200')),
                                                access_token=response['access_token'],
                                                v='5.122')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        if data['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE
        elif data['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        else:
            user.shopuserprofile.gender = ShopUserProfile.UNDEFINED

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        user.age = timezone.now().date().year - bdate.year
        if user.age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['domain']:
        user.shopuserprofile.vk_url = f"https://vk.com/{data['domain']}"

    # if data['photo_200']:
    #     user.avatar = Image.open(BytesIO(requests.get(data['photo_200']).content))

    # api_url = urlunparse(('https',
    #                       'api.vk.com',
    #                       '/method/account.getInfo',
    #                       None,
    #                       urlencode(OrderedDict(fields='lang',
    #                                             access_token=response['access_token'],
    #                                             v='5.122')),
    #                       None
    #                       ))
    #
    # resp = requests.get(api_url)
    # if resp.status_code != 200:
    #     return
    #
    # print(resp.json())
    # data = resp.json()['response'][0]
    # if data['lang']:
    #     user.shopuserprofile.lang = data['lang']

    user.save()
