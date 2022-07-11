from django.contrib.gis import admin
from world.models.world_border import WorldBorder

# Register your models here.
admin.site.register(WorldBorder, admin.GISModelAdmin)
