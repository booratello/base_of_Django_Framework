from django.urls import path
import mainapp.views as mainapp

app_name = 'gallery'

urlpatterns = [
    path('', mainapp.gallery, name='main'),
]
