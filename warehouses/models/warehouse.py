from django.db import models

from core.models import BaseModel


class Warehouse(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def location(self):
        return self.longitude, self.latitude
