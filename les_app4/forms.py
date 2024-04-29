from django import forms
from les_app2.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'descriptions', 'price', 'quantity', 'photo']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя продукта'}),
                   'descriptions': forms.TextInput(
                       attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
                   'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Кол-во'}),
                   }


class SavePhoto(forms.Form):
    photo = forms.ImageField()
