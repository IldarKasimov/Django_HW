from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_app3'),
    path('products/', views.get_products, name='get_products'),
    path('create_prod/<int:count>', views.create_products, name='create_products'),
    path('orders/', views.get_orders, name='get_orders'),
    path('create_ord/<int:client_id>', views.create_order, name='create_order'),
    path('del_ord/<int:order_id>', views.del_order, name='del_order'),
    path('add_prod/<int:order_id>', views.add_product, name='add_product'),
    path('prod_in_order/<int:order_id>/<int:product_id>/', views.prod_in_order, name='prod_in_order'),
    path('get_weak/<int:client_id>', views.get_weak, name='get_weak'),
]