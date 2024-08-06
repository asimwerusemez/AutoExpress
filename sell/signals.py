from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Cart

@receiver(post_save, sender=Cart)
def calculate_total_price(sender, instance, **kwargs):
    total_price_vehicule = Decimal(0)
    total_price_pieces = Decimal(0)

    for order in instance.order.all():
        if order.vehicule:
            total_price_vehicule += order.vehicule.prix * order.quatity
        elif order.piece:
            total_price_pieces += order.piece.prix * order.quatity

    instance.total_price = total_price_vehicule + total_price_pieces
    








