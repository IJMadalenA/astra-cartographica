from django.contrib.gis.db import models


class Shop(models.Model):
    name = models.CharField(
        max_length=120
    )
    # https://docs.djangoproject.com/en/4.1/ref/contrib/gis/model-api/#pointfield
    location = models.PointField()
    address = models.CharField(
        max_length=120
    )
    city = models.CharField(
        max_length=60
    )

