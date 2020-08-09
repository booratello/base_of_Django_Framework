import os
from math import ceil
from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def main(request):
    title = 'historical games'
    game_list = ['ASSASIN\'S CREED: Rogue', 'TOMB RAIDER', 'RYSE: Son Of Rome',
                 'WORLD OF WARCRAFT: Wrath Of The Linch King']
    products = [el for el in Product.objects.all() if el.name in game_list]
    html_names = [el[:-5] for el in filter(lambda x: x.endswith('.html'), os.listdir('mainapp/templates/mainapp'))]
    context = {'title': title, 'products': products, 'html_names': html_names}
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
    }
    return render(request, 'mainapp/contacts.html', context)


def gallery(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    title = 'gallery'
    category_menu = ProductCategory.objects.all()
    html_names = [el[:-5] for el in filter(lambda x: x.endswith('.html'), os.listdir('mainapp/templates/mainapp'))]
    context = {
        'title': title,
        'category_menu': category_menu,
        'html_names': html_names,
        'basket': basket
    }

    if pk is not None:
        if pk == 0:
            game_list = [el.name for el in Product.objects.all()]
        else:
            game_list = [el.name for el in Product.objects.filter(category_id=pk)]
        products = [
            [el for el in Product.objects.all() if el.name in game_list[multiple_four:multiple_four + 4]]
            for multiple_four in
            [num * 4 for num in range(ceil(len(game_list) / 4))]
        ]
        context['products'] = products
        return render(request, 'mainapp/gallery.html', context)

    game_list = ['BATTLEFIELD 1', 'STAR WARS Battlefront II', 'BATTLEFIELD 4', 'WORLD OF TANKS',
                 'ASSASIN\'S CREED: Rogue', 'FOR HONOR', 'WORLD OF WARSHIPS', 'CALL OF DUTY: Infinite Warface']
    products = [
        [el for el in Product.objects.all() if el.name in game_list[multiple_four:multiple_four + 4]]
        for multiple_four in
        [num * 4 for num in range(ceil(len(game_list) / 4))]
    ]
    context['products'] = products
    return render(request, 'mainapp/gallery.html', context)


def ac_rouge(request):
    title = 'assassin\'s creed: rogue'
    game_list = ['MIDDLE-EARTH: Shadow Of War', 'DISHONORED 2', 'THIEF', 'HITMAN']
    products = [el for el in Product.objects.all() if el.name in game_list]
    html_names = [el[:-5] for el in filter(lambda x: x.endswith('.html'), os.listdir('mainapp/templates/mainapp'))]
    context = {'title': title, 'products': products, 'html_names': html_names}
    return render(request, 'mainapp/ac_rouge.html', context)
