from django.db import models
from cars.models import Car

# Create your models here.
class  Order(models.Model):
    """
    Model to represent an order for a car.
    """
    name = models.CharField(max_length=100)
    cars = models.ManyToManyField(Car, related_name='orders')
    total =  models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.name)
        