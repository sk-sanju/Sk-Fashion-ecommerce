from django.db import models
import datetime

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id', blank=False, null=False)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField( upload_to='uploads/product/')
    
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.Product)