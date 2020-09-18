from django.urls import path, re_path
import mainapp.views as mainapp
from django.views.decorators.cache import cache_page


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('category/<int:pk>/', mainapp.gallery, name='category'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.gallery_ajax)),
    path('category/<int:pk>/<int:page>', mainapp.gallery, name='page'),
    re_path(r'^category/(?P<pk>\d+)/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.gallery_ajax)),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
