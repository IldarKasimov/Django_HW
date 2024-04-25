from django.urls import path
from .views import index, create_client, get_clients, du_client, del_client, update_client


urlpatterns = [
    path('', index, name='index_app1'),
    path('create_client/', create_client, name='create_client'),
    path('get_clients/', get_clients, name='get_clients'),
    path('du_client/', du_client, name='du_client'),
    path('<int:client_id>/del_client/', del_client, name='del_client'),
    path('<int:client_id>/update_client/', update_client, name='update_client'),
]