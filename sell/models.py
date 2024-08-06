from decimal import Decimal
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from car.models import Vehicule, Piece

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, blank=True, null=True)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE, blank=True, null=True)
    quatity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        name = ""
        if self.vehicule:
            name = self.vehicule.marque
        elif self.piece:
            name = self.piece.type_piece

        return f"{name}: ({self.quatity})"

    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)

    def __str__(self) -> str:
        return f"{self.user.username}"
    
    def delete(self, *args, **kwargs):
        for orders in self.order.all():
            orders.ordered = True
            orders.ordered_date = timezone.now()
            orders.save()
        
        self.order.clear()
        return super().delete(*args, **kwargs)
    
    def get_total_price(self):
        total_price_vehicule = Decimal(0)
        total_price_pieces = Decimal(0)

        for order in self.order.all():
            if order.vehicule:
                total_price_vehicule += order.vehicule.prix * order.quatity
            elif order.piece:
                total_price_pieces += order.piece.prix * order.quatity

        return total_price_pieces + total_price_vehicule


class LivraisonAdresse(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    adresse_livraison = models.TextField()

    def __str__(self):
        return f"L'adresse de livraison de {self.cart.user.username}"
    


class VenteCars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    channels = models.CharField(max_length=10)
    transaction_id = models.CharField(max_length=50)
    description = models.TextField()
    return_url = models.URLField()
    notify_url = models.URLField()
    customer_name = models.CharField(max_length=50)
    customer_surname = models.CharField(max_length=50)
    response = models.JSONField(null=True, blank=True)


    def __str__(self) -> str:
        return f'achat de {self.user}'
    
