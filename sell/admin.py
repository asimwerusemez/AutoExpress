from django.contrib import admin

from .models import VenteCars, Cart, Order, LivraisonAdresse

admin.site.register(VenteCars)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(LivraisonAdresse)
