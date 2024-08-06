# Generated by Django 5.0.7 on 2024-08-04 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculeOuPiece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('marque', models.CharField(blank=True, max_length=100, null=True)),
                ('modele', models.CharField(blank=True, max_length=100, null=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('etat', models.CharField(choices=[('Neuf', 'Neuf'), ('Occasion', 'Occasion')], default='Neuf', max_length=50)),
                ('photo', models.ImageField(upload_to='articles_images')),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('vehiculeoupiece_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='car.vehiculeoupiece')),
                ('type_piece', models.CharField(max_length=100)),
            ],
            bases=('car.vehiculeoupiece',),
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('vehiculeoupiece_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='car.vehiculeoupiece')),
                ('annee_fabrication', models.IntegerField()),
                ('kilometrage', models.IntegerField(blank=True, null=True)),
                ('carburant', models.CharField(max_length=50)),
                ('type_vehicule', models.CharField(max_length=50)),
            ],
            bases=('car.vehiculeoupiece',),
        ),
    ]