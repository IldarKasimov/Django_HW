from django.urls import path
from .views import main, about_me


urlpatterns = [
    path('', main, name='main'),
    path('about_me/', about_me, name='about_me'),
]