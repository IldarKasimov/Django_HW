from django.shortcuts import render, redirect
from les_app2.models import Product, Order, Client
from random import randint
from datetime import datetime


def index(request):
    return render(request, 'les_app3/index.html')


def get_products(request):
    if request.method == 'POST':
        count = request.POST.get('count', None)
        return redirect('create_products', count=count)
    products = Product.objects.all()
    return render(request, 'les_app3/products.html', {'products': products})


def create_products(request, count):
    start = Product.get_end()
    for i in range(start[0].id, start[0].id + count):
        product = Product(name=f'Product_{i}', descriptions=f'Descriptions-product_{i}', price=randint(50, 9999),
                          quantity=randint(1, 100))
        product.save()
    return redirect('get_products')


def get_orders(request):
    orders = Order.objects.all()
    clients = Client.objects.all()
    return render(request, 'les_app3/orders.html', {'orders': orders, 'clients': clients})


def create_order(request, client_id):
    client = Client.objects.get(pk=client_id)
    order = Order.objects.create(client=client, total_amount=0)
    order.save()
    return redirect('get_orders')


def del_order(request, order_id):
    order = Order.objects.filter(pk=order_id)
    order.delete()
    return redirect('get_orders')


def add_product(request, order_id):
    products = Product.objects.all()
    order_id = order_id
    return render(request, 'les_app3/add_products.html', {'order_id': order_id, 'products': products})


def prod_in_order(request, order_id, product_id):
    order = Order.objects.get(pk=order_id)
    product = Product.objects.get(pk=product_id)
    order.product.add(product)
    total_amount = 0
    for product in order.product.all():
        total_amount += product.price
    order.total_amount = total_amount
    order.save()
    return redirect('get_orders')


def get_weak(request, client_id):
    orders = Order.objects.filter(client=client_id)
    orders_list = []
    for order in orders:
        if (datetime.now().date() - order.date_order).days < 8:
            orders_list.append(order)
    return render(request, 'les_app3/weak.html', {'orders': orders_list})

