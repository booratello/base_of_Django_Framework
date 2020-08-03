import os
from django.shortcuts import render
from mainapp.models import Product, ProductCategory


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


def gallery(request):
    title = 'gallery'
    game_list = ['BATTLEFIELD 1', 'STAR WARS Battlefront II', 'BATTLEFIELD 4', 'WORLD OF TANKS',
                 'ASSASIN\'S CREED: Rogue', 'FOR HONOR', 'WORLD OF WARSHIPS', 'CALL OF DUTY: Infinite Warface']
    products = [el for el in Product.objects.all() if el.name in game_list]
    html_names = [el[:-5] for el in filter(lambda x: x.endswith('.html'), os.listdir('mainapp/templates/mainapp'))]
    context = {'title': title, 'products_1': products[:4], 'products_2': products[4:], 'html_names': html_names}
    return render(request, 'mainapp/gallery.html', context)


def ac_rouge(request):
    title = 'assassin\'s creed: rogue'
    game_list = ['MIDDLE-EARTH: Shadow Of War', 'DISHONORED 2', 'THIEF', 'HITMAN']
    products = [el for el in Product.objects.all() if el.name in game_list]
    html_names = [el[:-5] for el in filter(lambda x: x.endswith('.html'), os.listdir('mainapp/templates/mainapp'))]
    context = {'title': title, 'products': products, 'html_names': html_names}
    return render(request, 'mainapp/ac_rouge.html', context)
