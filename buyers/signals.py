## set a  signal  between   the  user  and buyer model

## this signal will create a buyer model instance when a user is created

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer

@receiver(post_save, sender=User)
def  post_save_create_buyer(sender, instance, created, **kwargs):
    ## instace is the user instance
    ##  created is boolean value : true or false
    
    print(sender)
    print(instance)
    print(created) 
    
    if created:
        ## create a buyer instance
        Buyer.objects.create(user=instance, from_signal=True)
        print(f"Buyer created for user: {instance.username}")