from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False) ## for learning purpioses
    
    def __str__(self):
        return f"{self.user}"
    