from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_products/', views.get_products, name='get_products'),
    path('update_product/<int:product_id>', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('create_product/', views.create_product, name='create_product'),
    path('add_photo/<int:product_id>', views.add_photo, name='add_photo'),
]
