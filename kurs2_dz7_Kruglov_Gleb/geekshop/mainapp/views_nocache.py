from math import ceil
from random import sample

from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_rnd_product():
    products_list = Product.objects.filter(category__is_active=True, is_active=True)
    return sample(list(products_list), 4)


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:4]
    return same_products


def main(request):
    title = 'historical games'
    game_list = get_rnd_product()
    products = [el for el in Product.objects.all() if el in game_list]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
    }
    return render(request, 'mainapp/contacts.html', context)


def gallery(request, pk=None, page=1):
    title = 'gallery'
    category_menu = ProductCategory.objects.filter(is_active=True)

    context = {
        'title': title,
        'category_menu': category_menu,
    }

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'all'
            }

            game_list = [el.name for el in Product.objects.filter(category__is_active=True, is_active=True)]
            products = [
                [el for el in Product.objects.all() if el.name in game_list[multiple_four:multiple_four + 4]]
                for multiple_four in
                [num * 4 for num in range(ceil(len(game_list) / 4))]
            ]
            context['products'] = products
        else:
            game_list = [el.name for el in Product.objects.filter(category_id=pk, category__is_active=True, is_active=True)]
            is_category_empty = ProductCategory.objects.get(pk=pk)
            if len(game_list) == 0 and is_category_empty.is_active is True:
                is_category_empty.is_active = False
                is_category_empty.save()

            category = get_object_or_404(ProductCategory, pk=pk, is_active=True)
            products = [el for el in Product.objects.all() if el.name in game_list]
            paginator = Paginator(products, 2)
            try:
                products_paginator = paginator.page(page)
            except PageNotAnInteger:
                products_paginator = paginator.page(1)
            except EmptyPage:
                products_paginator = paginator.page(paginator.num_pages)
            context['products'] = products_paginator

        context['category'] = category
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
    product = get_object_or_404(Product, pk=pk, is_active=True, category__is_active=True)

    title = product.name
    game_list = [el.name for el in get_same_products(product)]
    products = [el for el in Product.objects.all() if el.name in game_list]
    context = {
        'title': title,
        'product': product,
        'products': products,
    }

    return render(request, 'mainapp/product.html', context)
