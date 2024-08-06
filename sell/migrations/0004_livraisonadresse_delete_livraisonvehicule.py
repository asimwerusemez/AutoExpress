# Generated by Django 5.0.7 on 2024-08-05 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_cart_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='LivraisonAdresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_livraison', models.TextField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.cart')),
            ],
        ),
        migrations.DeleteModel(
            name='LivraisonVehicule',
        ),
    ]