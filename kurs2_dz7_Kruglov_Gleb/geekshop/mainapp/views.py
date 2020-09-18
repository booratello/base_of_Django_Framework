from math import ceil
from random import sample

from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page, never_cache
from django.template.loader import render_to_string
from django.http import JsonResponse


def get_products_for_pseudocategories():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__is_active=True, is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
       return Product.objects.filter(category__is_active=True, is_active=True).select_related('category')

# Ломается сайт
# def get_category(pk):
#     if settings.LOW_CACHE:
#        key = f'category_{pk}'
#        category = cache.get(key)
#         if category is None:
#             category = get_object_or_404(ProductCategory, pk=pk, is_active=True)
#             cache.set(key, category)
#         return category
#     else:
#         return category = get_object_or_404(ProductCategory, pk=pk, is_active=True)


def get_products_for_categories(pk):
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category_id=pk, category__is_active=True, is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
       return Product.objects.filter(category_id=pk, category__is_active=True, is_active=True).select_related('category')

# Ломается сайт
# def get_product(pk):
#     if settings.LOW_CACHE:
#         key = f'product_{pk}'
#         product = cache.get(key)
#         if product is None:
#             product = get_object_or_404(Product, pk=pk, is_active=True, category__is_active=True)
#             cache.set(key, product)
#         return product
#    else:
#         return get_object_or_404(Product, pk=pk, is_active=True, category__is_active=True)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_rnd_product():
    # products_list = Product.objects.filter(category__is_active=True, is_active=True)
    products_list = get_products_for_pseudocategories()
    return sample(list(products_list), 4)


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:4]
    return same_products


def main(request):
    title = 'historical games'
    game_list = get_rnd_product()
    products = [el for el in Product.objects.all().select_related() if el in game_list]
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


# @never_cache
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
            game_list = [el.name for el in get_products_for_pseudocategories()]
            products = [
                [el for el in Product.objects.all().select_related() if el.name in game_list[multiple_four:multiple_four + 4]]
                for multiple_four in
                [num * 4 for num in range(ceil(len(game_list) / 4))]
            ]
            context['products'] = products
        else:
            game_list = [el.name for el in Product.objects.filter(category_id=pk, category__is_active=True, is_active=True)]
            # game_list = [el.name for el in get_products_for_categories(pk)]
            is_category_empty = ProductCategory.objects.get(pk=pk)
            if len(game_list) == 0 and is_category_empty.is_active is True:
                is_category_empty.is_active = False
                is_category_empty.save()

            category = get_object_or_404(ProductCategory, pk=pk, is_active=True)
            products = [el for el in Product.objects.all().select_related() if el.name in game_list]
            paginator = Paginator(products, 2)
            try:
                products_paginator = paginator.page(page)
            except PageNotAnInteger:
                products_paginator = paginator.page(1)
            except EmptyPage:
                products_paginator = paginator.page(paginator.num_pages)
            context['products'] = products_paginator

        context['category'] = category
        # context['category'] = get_category(pk)
        return render(request, 'mainapp/gallery.html', context)

    context['hot_product'] = get_rnd_product()[0]
    game_list = get_same_products(context['hot_product'])

    products = [
        [el for el in Product.objects.all().select_related() if el in game_list[multiple_four:multiple_four + 4]]
        for multiple_four in
        [num * 4 for num in range(ceil(len(game_list) / 4))]
    ]

    context['products'] = products

    return render(request, 'mainapp/gallery.html', context)


# @never_cache
def gallery_ajax(request, pk=None, page=1):
    if request.is_ajax():
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

                # game_list = [el.name for el in Product.objects.filter(category__is_active=True, is_active=True)]
                game_list = [el.name for el in get_products_for_pseudocategories()]
                products = [
                    [el for el in Product.objects.all().select_related() if el.name in game_list[multiple_four:multiple_four + 4]]
                    for multiple_four in
                    [num * 4 for num in range(ceil(len(game_list) / 4))]
                ]
                context['products'] = products
            else:
                game_list = [el.name for el in Product.objects.filter(category_id=pk, category__is_active=True, is_active=True)]
                # game_list = [el.name for el in get_products_for_categories(pk)]
                is_category_empty = ProductCategory.objects.get(pk=pk)
                if len(game_list) == 0 and is_category_empty.is_active is True:
                    is_category_empty.is_active = False
                    is_category_empty.save()

                category = get_object_or_404(ProductCategory, pk=pk, is_active=True)
                products = [el for el in Product.objects.all().select_related() if el.name in game_list]
                paginator = Paginator(products, 2)
                try:
                    products_paginator = paginator.page(page)
                except PageNotAnInteger:
                    products_paginator = paginator.page(1)
                except EmptyPage:
                    products_paginator = paginator.page(paginator.num_pages)
                context['products'] = products_paginator

            context['category'] = category
            # context['category'] = get_category(pk)
            result = render_to_string(
                'mainapp/include/inc_gallery_content.html',
                context=context,
                request=request)

            return JsonResponse({'result': result})

        context['hot_product'] = get_rnd_product()[0]
        game_list = get_same_products(context['hot_product'])

        products = [
            [el for el in Product.objects.all().select_related() if el in game_list[multiple_four:multiple_four + 4]]
            for multiple_four in
            [num * 4 for num in range(ceil(len(game_list) / 4))]
        ]

        context['products'] = products

        result = render_to_string(
            'mainapp/include/inc_gallery_content.html',
            context=context,
            request=request)

        return JsonResponse({'result': result})


# @never_cache
@login_required
def product(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True, category__is_active=True)
    # product = get_product(pk)

    title = product.name
    game_list = [el.name for el in get_same_products(product)]
    products = [el for el in Product.objects.all().select_related() if el.name in game_list]
    context = {
        'title': title,
        'product': product,
        'products': products,
    }

    return render(request, 'mainapp/product.html', context)
