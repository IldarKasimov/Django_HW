from django.urls import path
from .views import main, about_me

urlpatterns = [
    path('', main,  name='index'),
    path('about/', about_me, name='about'),
]
