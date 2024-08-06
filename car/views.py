from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator

from .models import Vehicule, Piece


def cars_view(request):
    cars = Vehicule.objects.filter().order_by("-date_ajout")[:9]
    partsAutos = Piece.objects.filter().order_by("-date_ajout")[:6]
    return render(request, "cars/all_car.html", {
        "cars": cars,
        "partsAutos": partsAutos,
    })

def cars_details(request, id):
    car_detail = get_object_or_404(Vehicule, id=id)
    cars = Vehicule.objects.all()
    return render(request, "cars/detail_car.html", {"car_detail": car_detail, "cars": cars})

def pieces_details(request, id):
    piece_detail = get_object_or_404(Piece, id=id)
    partsAutos = Piece.objects.all()
    return render(request, "cars/piece_detail.html", {"piece_detail": piece_detail, "partsAutos": partsAutos})

def all_car(request):
    cars = Vehicule.objects.all()
    item_name = request.GET.get("item_name")
    if item_name != '' and item_name is not None:
        cars = Vehicule.objects.filter(marque__icontains=item_name)
    return render(request, "cars/cars.html", {"cars": cars})

def all_pieces(request):
    partsAutos = Piece.objects.all()

    item_name = request.GET.get("item_name")
    if item_name != '' and item_name is not None:
        partsAutos = Piece.objects.filter(marque__icontains=item_name)
    return render(request, "cars/pieces.html", {"partsAutos": partsAutos})