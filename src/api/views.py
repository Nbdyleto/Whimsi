from django.shortcuts import render
from rest_framework import generics
from .serializers import PropertySerializer
from whimsi.models import Property, PropertyAddress, PropertyImage

class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'slug'

class SearchResultsListView(generics.ListAPIView):
    model = Property
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.all()

        region = self.request.GET.get('region')
        if region:
            queryset = queryset.filter(propertyaddress__region__region_name=region)

        bedrooms = self.request.GET.get('bedrooms')
        if bedrooms:
            queryset = queryset.filter(bedrooms=bedrooms)

        type = self.request.GET.get('type')
        if type:
            queryset = queryset.filter(type=type)

        max_val = self.request.GET.get('max_value')
        if max_val:
            queryset = queryset.filter(price__lte=max_val)

        if not (region or bedrooms or type or max_val):
            queryset = Property.objects.all()
        
        return queryset