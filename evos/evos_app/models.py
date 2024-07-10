from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_quantity = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food.name} - {self.user.username}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}"

class OrderElement(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food.name} - {self.order.user.username}"



