from django.contrib import admin

# Register your models here.
from evos_app.models import Category, Food, Basket, Order, OrderElement

admin.site.register(Category),
admin.site.register(Food),
admin.site.register(Basket),
admin.site.register(Order),
admin.site.register(OrderElement)
