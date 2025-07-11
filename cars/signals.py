from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Car
from buyers.models import Buyer
import uuid

# @receiver(pre_save, sender=Car)
# def pre_save_generate_code_and_modify_buyer(sender, instance, **kwargs):
#     """
#     Signal to generate a unique code for the Car instance before saving.
#     """
#     if instance.code is None or instance.code == "":
#         instance.code = str(uuid.uuid4()).replace("-","").upper()[:10] 
    
#     obj = Buyer.objects.get(user=instance.buyer.user)
#     obj.from_signal = True
#     obj.save()

@receiver(post_save, sender=Car)
def post_save_generate_code_and_modify_buyer(sender, instance, created, **kwargs):
    """
    Signal to generate a unique code for the Car instance before saving.
    """
    if instance.code is None or instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-","").upper()[:10] 
        instance.save()  # Save the instance to update the code
    
    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()