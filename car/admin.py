from django.contrib import admin
from .models import Piece, Vehicule

class PicesTable(admin.ModelAdmin):
    list_display = ("marque", "prix", "date_ajout")

class VehiculeTable(admin.ModelAdmin):
    list_display = ("marque", "modele", "prix", "etat", "date_ajout")

admin.site.register(Piece, PicesTable)
admin.site.register(Vehicule, VehiculeTable)

