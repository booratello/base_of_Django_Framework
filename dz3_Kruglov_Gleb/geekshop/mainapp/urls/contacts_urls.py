from django.urls import path
import mainapp.views as mainapp

app_name = 'contacts'

urlpatterns = [
    path('', mainapp.contacts, name='main'),
]
