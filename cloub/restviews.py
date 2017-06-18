from rest_framework import viewsets
from .models import *
from .serializer import Equipment_class_serializer

class Euipment_class_set(viewsets.ModelViewSet):
    queryset = Equipment_class.objects.all()
    serializer_class = Equipment_class_serializer
    