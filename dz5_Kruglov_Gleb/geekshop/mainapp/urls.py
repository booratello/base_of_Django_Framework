from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('<int:pk>/', mainapp.gallery, name='category'),
]
