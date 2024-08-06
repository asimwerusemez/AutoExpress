from django.urls import path
from .views import achatCar, cart, payment_confirmation, add_to_cart_car, add_to_cart_piece


app_name = "sell"

urlpatterns = [
    path("achatCar/<int:id>", achatCar, name="achatCar"),
    path("article/<int:id>/add-to-cart-vehicule", add_to_cart_car, name="add_to_cart_car"),
    path("article/<int:id>/add-to-cart_piece", add_to_cart_piece, name="add_to_cart_piece"),
    path("cart", cart, name="cart"),
    path("achatCar/<int:id>", achatCar, name="achatCar"),
    path("payment_confirmation", payment_confirmation, name="payment_confirmation"),
]