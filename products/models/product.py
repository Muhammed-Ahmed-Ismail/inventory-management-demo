from django.db import models

from core.models import CodedBaseModel


class Product(CodedBaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)