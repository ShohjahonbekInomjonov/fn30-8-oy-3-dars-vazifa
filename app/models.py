from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.username
    

class Restaurant(models.Model):
    CATEGORIES = [
        ('mil', 'Milliy Taomlar'),
        ('tur', 'Turkish Restaurant'),
        ('caf', 'Cafe')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    photo = models.ImageField(upload_to="images/restaurant", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    category = models.CharField(max_length=3, choices=CATEGORIES)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/dish", null=True, blank=True)
    prep_time = models.ImageField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    register_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment = models.ForeignKey("Payment", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    paid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.dish.name} to {self.delivery_address}"


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Driver(models.Model):
    fullname = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    transport_type = models.CharField(max_length=255)
    is_aviable = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=255)
    estimated_delivery_time = models.DateTimeField(auto_now_add=True)
    actual_delivery_time = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.fullname} {self.delivery_fee}"