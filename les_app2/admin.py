from django.contrib import admin
from .models import Client, Product, Order
from datetime import datetime
from django.utils.html import mark_safe


@admin.action(description='Сбросить номер телефона')
def reset_phone(modeladmin, request, queryset):
    queryset.update(phone='')


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_registration', 'phone', 'email']
    ordering = ['name', '-date_registration']
    list_filter = ['date_registration']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (Name)'
    actions = [reset_phone]

    readonly_fields = ['email', 'date_registration']
    fieldsets = [
        (
            'Имя',
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Данные',
            {
                'classes': ['collapse'],
                'description': 'Данные клиента',
                'fields': ['date_registration', 'phone', 'email'],
            },
        )
    ]


@admin.action(description='Установить текущую дату')
def qet_data_now(modeladmin, request, queryset):
    queryset.update(date_order=datetime.now())


@admin.action(description='Обнулить количество')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_order', 'client', 'product_display', 'date_order']
    list_filter = ['client']
    actions = [qet_data_now]

    def get_order(self, obj):
        return f'Заказ - {obj.id}'

    get_order.short_description = 'Номер заказа'

    def product_display(self, odj):
        return ', '.join([product.name for product in odj.product.all()])

    readonly_fields = ['get_order', 'date_order']
    fieldsets = [
        (
            'Номер заказа',
            {
                'classes': ['wide'],
                'fields': ['get_order'],
            }
        ),
        (
            'Данные',
            {
                'fields': ['client', 'product', 'total_amount', 'date_order'],
            }
        )
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'display_image', ]
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    actions = [reset_quantity]
    ordering = ['price', '-quantity']

    readonly_fields = ['display_image', 'name']
    fieldsets = [
        (
            'Имя товара',
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Информация',
            {
                'description': 'Инфо о товаре',
                'fields': ['descriptions', 'price', 'quantity', 'display_image']
            }
        )
    ]

    def display_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width=50 height=50>')

    display_image.short_description = 'Изображение'


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
