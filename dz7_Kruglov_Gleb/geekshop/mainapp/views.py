from math import ceil
from random import sample
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_rnd_product():
    products_list = Product.objects.filter(category__is_active=True)
    return sample(list(products_list), 4)


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:4]
    return same_products


def main(request):
    title = 'historical games'
    game_list = get_rnd_product()
    products = [el for el in Product.objects.all() if el in game_list]
    context = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contacts.html', context)


def gallery(request, pk=None):
    title = 'gallery'
    basket = get_basket(request.user)
    category_menu = ProductCategory.objects.all()
    context = {
        'title': title,
        'category_menu': category_menu,
        'basket': basket
    }

    if pk is not None:
        if pk == 0:
            game_list = [el.name for el in Product.objects.filter(category__is_active=True)]
        else:
            game_list = [el.name for el in Product.objects.filter(category_id=pk)]
        products = [
            [el for el in Product.objects.all() if el.name in game_list[multiple_four:multiple_four + 4]]
            for multiple_four in
            [num * 4 for num in range(ceil(len(game_list) / 4))]
        ]
        context['products'] = products
        return render(request, 'mainapp/gallery.html', context)

    context['hot_product'] = get_rnd_product()[0]
    game_list = get_same_products(context['hot_product'])

    products = [
        [el for el in Product.objects.all() if el in game_list[multiple_four:multiple_four + 4]]
        for multiple_four in
        [num * 4 for num in range(ceil(len(game_list) / 4))]
    ]
    context['products'] = products

    return render(request, 'mainapp/gallery.html', context)


@login_required
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = product.name
    game_list = [el.name for el in get_same_products(product)]
    products = [el for el in Product.objects.all() if el.name in game_list]
    context = {
        'title': title,
        'basket': get_basket(request.user),
        'product': product,
        'products': products,
    }
    return render(request, 'mainapp/product.html', context)
