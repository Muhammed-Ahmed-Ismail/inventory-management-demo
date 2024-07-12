from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CodedBaseModel(BaseModel):
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        abstract = True
