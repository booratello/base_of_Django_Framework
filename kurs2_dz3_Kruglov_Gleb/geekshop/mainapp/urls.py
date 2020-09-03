from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('category/<int:pk>/', mainapp.gallery, name='category'),
    path('category/<int:pk>/<int:page>', mainapp.gallery, name='page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
