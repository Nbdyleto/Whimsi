from django.shortcuts import render
from rest_framework import generics
from .serializers import PropertySerializer
from whimsi.models import Property

class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'slug'