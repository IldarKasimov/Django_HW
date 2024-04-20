from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']


class ClientDel(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone']