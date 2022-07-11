from django.contrib.gis import admin
from .models.shop import Shop


@admin.register(Shop)
class ShopAdmin(admin.GeoModelAdmin):
    list_display = (
        'name',
        'location',
    )

