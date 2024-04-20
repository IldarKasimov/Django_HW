from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Client


def index(request):
    return render(request, 'index.html')


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_clients')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


def get_clients(request):
    clients = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients})


def du_client(request):
    client = Client.objects.all()
    return render(request, 'du_client.html', {'clients': client})


def del_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('du_client')
    return None


def update_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('du_client')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})
