from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from sellCar import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("car.urls")),
    path("sell/", include("sell.urls")),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
