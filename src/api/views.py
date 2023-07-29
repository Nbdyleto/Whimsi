from django.shortcuts import render
from rest_framework import generics
from .serializers import PropertySerializer
from whimsi.models import Property

class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'slug'

class SearchResultsListView(generics.ListAPIView):
    model = Property
    serializer_class = PropertySerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        print('query: ', query)
        return Property.objects.filter(
            title__icontains=query
        )