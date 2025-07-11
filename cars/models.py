from django.db import models
from buyers.models import Buyer
import uuid
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=200)
    price  = models.PositiveIntegerField()
    buyer = models.ForeignKey(
       Buyer, 
        on_delete=models.CASCADE, 
        related_name='cars'
    ) 
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyer}"
    
    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = str(uuid.uuid4()).replace("-","").upper()[:10]  # Generate a unique code if not provided
        return super().save(*args, **kwargs)
