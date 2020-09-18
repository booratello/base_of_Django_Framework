from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from authapp.forms import ShopUserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm


# @user_passes_test(lambda user: user.is_superuser)
# def user_create(request):
#     title = 'user / create'
#     if request.method == 'POST':
#         update_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         update_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'form': update_form
#     }
#     return render(request, 'adminapp/user_update.html', context)


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'user / create'
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def users(request):
#     title = 'admin / users'
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     context = {
#         'title': title,
#         'object_list': users_list
#     }
#     return render(request, 'adminapp/users.html', context)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'admin / users'
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def user_update(request, pk):
#     title = 'user / update'
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         update_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         update_form = ShopUserAdminEditForm(instance=edit_user)
#
#     context = {
#         'title': title,
#         'form': update_form
#     }
#     return render(request, 'adminapp/user_update.html', context)


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'category / update'
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def user_delete(request, pk):
#     title = 'user / delete'
#
#     user_item = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user_item.is_active = False
#         user_item.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#
#     context = {
#         'title': title,
#         'user_to_delete': user_item
#     }
#     return render(request, 'adminapp/user_delete.html', context)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'user / delete'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda user: user.is_superuser)
# def category_create(request):
#     title = 'category / create'
#     if request.method == 'POST':
#         update_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         update_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'form': update_form
#     }
#     return render(request, 'adminapp/category_update.html', context)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'category / create'
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def categories(request):
#     title = 'admin / categories'
#     categories_list = ProductCategory.objects.all().order_by('-is_active', '-id')
#     context = {
#         'title': title,
#         'object_list': categories_list
#     }
#     return render(request, 'adminapp/categories.html', context)


class ProductCategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, page=1, **kwargs):
        context = super().get_context_data()
        context['title'] = 'admin / categories'
        category_list = ProductCategory.objects.all().order_by('-is_active', '-id')
        # paginator = Paginator(category_list, 3)
        # try:
        #     categories_paginator = paginator.page(page)
        # except PageNotAnInteger:
        #     categories_paginator = paginator.page(1)
        # except EmptyPage:
        #     categories_paginator = paginator.page(paginator.num_pages)
        # context['object_list'] = categories_paginator
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def category_update(request, pk):
#     title = 'category / update'
#
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_item)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         update_form = ProductCategoryEditForm(instance=category_item)
#
#     context = {
#         'title': title,
#         'form': update_form
#     }
#     return render(request, 'adminapp/category_update.html', context)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'category / update'
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def category_delete(request, pk):
#     title = 'category / delete'
#
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_item.is_active = False
#         category_item.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': category_item
#     }
#     return render(request, 'adminapp/category_delete.html', context)

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'category / delete'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda user: user.is_superuser)
def product_create(request, pk):
    title = 'product / create'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        create_product = ProductEditForm(request.POST, request.FILES)
        if create_product.is_valid():
            create_product.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        create_product = ProductEditForm()

    context = {
        'title': title,
        'form': create_product,
        'category': category
    }
    return render(request, 'adminapp/product_update.html', context)


# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductEditForm
#     template_name = 'adminapp/category_update.html'
#     success_url = reverse_lazy('admin:products')
#
#     @method_decorator(user_passes_test(lambda user: user.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'product / create'
#         context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
#
#         return context


# @user_passes_test(lambda user: user.is_superuser)
# def product_read(request, pk):
#     title = 'product / more'
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'title': title,
#         'object_list': product,
#     }
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'product / more'
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def products(request, pk):
#     title = 'admin / products'
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category=category_item)
#     context = {
#         'title': title,
#         'object_list': products_list,
#         'category': category_item
#     }
#     return render(request, 'adminapp/products.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'admin / products'
        context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context['object_list'] = Product.objects.filter(category=context['category'])
        return context


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, pk):
    title = 'product / update'
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    context = {
        'title': title,
        'form': edit_form,
        'category': edit_product.category
    }
    return render(request, 'adminapp/product_update.html', context)


# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductEditForm
#     template_name = 'adminapp/category_update.html'
#     success_url = reverse_lazy('admin:product_update')
#
#     @method_decorator(user_passes_test(lambda user: user.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'product / update'
#         context['category'] = get_object_or_404(Product, pk=self.kwargs['pk']).category
#         return context


# @user_passes_test(lambda user: user.is_superuser)
# def product_delete(request, pk):
#     title = 'product / delete'
#
#     delete_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         delete_product.is_active = False
#         delete_product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[delete_product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': delete_product
#     }
#     return render(request, 'adminapp/product_delete.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'


    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'product / delete'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        self.success_url = reverse_lazy('admin:products', args=[self.object.category.pk])
        return HttpResponseRedirect(self.get_success_url())
