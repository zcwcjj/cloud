from .models import *
from rest_framework import serializers


class Equipment_class_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment_class
        fields = ('name',)





