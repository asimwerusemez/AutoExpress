from django.urls import path
from .views import cars_view, cars_details, pieces_details, all_car, all_pieces

app_name = "car"

urlpatterns = [
    path("", cars_view, name="cars_view"),
    path("cars_details/<int:id>", cars_details, name="cars_details"),
    path("pieces_details/<int:id>", pieces_details, name="pieces_details"),
    path("all_car", all_car, name="all_car"),
    path("all_pieces", all_pieces, name="all_pieces"),
]
