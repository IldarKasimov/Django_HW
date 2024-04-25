from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    date_registration = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_end():
        value = Product.objects.order_by('-id')[:1]
        return value


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.deletion.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)
