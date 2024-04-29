from django.shortcuts import render, redirect
from les_app2.models import Product, Order, Client
from random import randint
from datetime import datetime


def index(request):
    return render(request, 'les_app3/index.html')


def get_products(request):
    if request.method == 'POST':
        count = request.POST.get('count', None)
        if not count:
            count = 0
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


def get_list_product(request, client_id):
    orders = Order.objects.filter(client=client_id)
    client = Client.objects.get(pk=client_id)
    client_name = client.name
    context = {'orders': orders, 'text': 'все время', 'client_name': client_name}
    if request.method == 'POST':
        days = request.POST.get('days', None)
        if not days:
            return render(request, 'les_app3/list_product.html', context=context)
        days = int(days)
        if days == 1:
            text = 'сегодня'
        elif (days // 10) % 10 == 1 or days % 10 == 0 or 5 <= days % 10 <= 9:
            text = f'последние {days} дней'
        elif 2 <= days % 10 <= 4:
            text = f'последние {days} дня'
        else:
            text = f'последний {days} день'
        orders_list = []
        for order in orders:
            if (datetime.now().date() - order.date_order).days < days:
                orders_list.append(order)
        product_list = []
        for order in orders_list:
            for product in order.product.all():
                if product.name not in product_list:
                    product_list.append(product.name)
        context = {'orders': orders_list, 'text': text, 'list': product_list, 'client_name': client_name}
        return render(request, 'les_app3/list_product.html', context=context)
    return render(request, 'les_app3/list_product.html', context=context)
