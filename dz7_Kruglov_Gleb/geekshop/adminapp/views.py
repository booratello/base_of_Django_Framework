from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from authapp.forms import ShopUserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    title = 'user / create'
    if request.method == 'POST':
        update_form = ShopUserRegisterForm(request.POST, request.FILES)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        update_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'update_form': update_form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def users(request):
    title = 'admin / users'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    context = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    title = 'user / update'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        update_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        update_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        'title': title,
        'update_form': update_form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    title = 'user / delete'

    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_item.is_active = False
        user_item.save()
        return HttpResponseRedirect(reverse('admin:users'))

    context = {
        'title': title,
        'user_to_delete': user_item
    }
    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda user: user.is_superuser)
def category_create(request):
    title = 'category / create'
    if request.method == 'POST':
        update_form = ProductCategoryEditForm(request.POST, request.FILES)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        update_form = ProductCategoryEditForm()

    context = {
        'title': title,
        'update_form': update_form
    }
    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def categories(request):
    title = 'admin / categories'
    categories_list = ProductCategory.objects.all().order_by('-is_active', '-id')
    context = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda user: user.is_superuser)
def category_update(request, pk):
    title = 'category / update'

    category_item = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        update_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_item)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        update_form = ProductCategoryEditForm(instance=category_item)

    context = {
        'title': title,
        'update_form': update_form
    }
    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def category_delete(request, pk):
    title = 'user / delete'

    category_item = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_item.is_active = False
        category_item.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    context = {
        'title': title,
        'category_to_delete': category_item
    }
    return render(request, 'adminapp/category_delete.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def products(request, pk):
    title = 'admin / products'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item)
    context = {
        'title': title,
        'objects': products_list,
        'category': category_item
    }
    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, pk):
    pass
