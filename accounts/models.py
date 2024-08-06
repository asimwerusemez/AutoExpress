from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=10)
    adresse = models.TextField()

    def __str__(self):
        return self.username
