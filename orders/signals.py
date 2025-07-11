from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Order
from sales.models import Sales

@receiver(m2m_changed, sender=Order.cars.through)
def update_order_total_car_m2m(sender, instance, action, **kwargs):
    print("Signal triggered for m2m_changed on Order.cars")
    print(f"Action: {action}")
    total = 0
    total_price = 0
    if  action == "post_add" or action == "post_remove":
        for car in instance.cars.all():
            total +=1
            total_price += car.price
            
        instance.total = total
        instance.total_price = total_price
        instance.save()

@receiver(post_save, sender=Order)
def post_save_create_update_sale(sender, instance, created, **kwargs):
    """
    Signal to create or update a Sales instance after an Order is saved.
    """
    obj, _ = Sales.objects.get_or_create(order=instance)
    obj.amount = instance.total_price
    obj.save()
    
    