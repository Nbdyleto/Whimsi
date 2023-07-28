import requests

from django.shortcuts import render
from .models import Property, HighlightedProperty

def home_view(request):
    last_properties = Property.objects.order_by('-created_at')[:3]
    highlighted_properties = HighlightedProperty.objects.prefetch_related('property__propertyaddress').all()

    context = {
        'last_properties': last_properties,
        'highlighted_properties': highlighted_properties,
    }
    
    return render(request, 'templates/pages/home.html', context)

def properties_template(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'templates/pages/properties.html', context)

def property_detail_template(request, slug):
    api_url = f"http://127.0.0.1:8000/api/properties/{slug}/"
    response = requests.get(api_url)
    property_data = response.json() if response.status_code == 200 else None

    context = {
        'property': property_data,
    }

    return render(request, 'templates/pages/property.html', context)