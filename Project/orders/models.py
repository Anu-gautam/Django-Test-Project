from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem, through='OrderItem')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")])
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
