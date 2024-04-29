from django.shortcuts import render, redirect, get_object_or_404
from les_app2.models import Product
from .forms import ProductForm, SavePhoto


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
    product = get_object_or_404(Product, id=product_id)
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


def add_photo(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form_photo = SavePhoto(request.POST, request.FILES)
        if form_photo.is_valid():
            photo = form_photo.cleaned_data['photo']
            product.photo = photo
            product.save()
        return get_products(request)
    else:
        form = SavePhoto()
    return render(request, 'les_app4/add_photo.html', {'form': form})
