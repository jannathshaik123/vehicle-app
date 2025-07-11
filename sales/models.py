from django.db import models
from orders.models import Order
# Create your models here.

class Sales(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='sales')
    amount = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.amount)