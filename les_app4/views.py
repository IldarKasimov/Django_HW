from django.shortcuts import render, redirect
from les_app2.models import Product
from .forms import ProductForm


def index(request):
    return render(request, 'les_app4/index.html')


def get_products(request):
    products = Product.objects.all()
    return render(request, 'les_app4/products.html', {'products': products})


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('get_products')
    else:
        form = ProductForm(instance=product)
    context = {'form': form, 'product': product, 'title': 'Изменить товар'}
    return render(request, 'les_app4/form_product.html.html', context=context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return get_products(request)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return get_products(request)
    else:
        form = ProductForm()
    context = {'form': form, 'title': 'Создать товар'}
    return render(request, 'les_app4/form_product.html.html', context=context)