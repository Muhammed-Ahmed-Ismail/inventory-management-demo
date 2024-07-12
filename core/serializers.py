from rest_framework import serializers

from core.models import BaseModel, CodedBaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
        abstract = True


class CodedBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodedBaseModel
        fields = '__all__'
        abstract = True
