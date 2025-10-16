from django.contrib import admin
from .models import User, Restaurant, Customer, Delivery, Dish, Driver, Menu, Order, Payment, Review
# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Delivery)
admin.site.register(Dish)
admin.site.register(Driver)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Payment)