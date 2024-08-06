from django.db import models

class VehiculeOuPiece(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    marque = models.CharField(max_length=100, blank=True, null=True)
    modele = models.CharField(max_length=100, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    etat = models.CharField(max_length=50, choices=[('Neuf', 'Neuf'), ('Occasion', 'Occasion')], default='Neuf')
    photo = models.ImageField(upload_to="articles_images")

class Vehicule(VehiculeOuPiece):
    annee_fabrication = models.IntegerField()
    kilometrage = models.IntegerField(blank=True, null=True)
    carburant = models.CharField(max_length=50)
    type_vehicule = models.CharField(max_length=50)

class Piece(VehiculeOuPiece):
    type_piece = models.CharField(max_length=100)




