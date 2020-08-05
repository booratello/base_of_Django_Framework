from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('gallery/', mainapp.gallery, name='gallery'),
    path('contacts/', mainapp.contacts, name='contacts'),
]
