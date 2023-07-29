import requests

from django.shortcuts import render
from .models import Property, HighlightedProperty, PropertyImage

def home_view(request):
    last_properties = Property.objects.order_by('-created_at')[:3]
    print('Last properties:')
    for property in last_properties:
        property.first_image = PropertyImage.objects.filter(property=property).first()
    
    highlighted_properties = HighlightedProperty.objects.prefetch_related('property__propertyaddress').all()
    print('Highlighted Properties:')
    for property in highlighted_properties:
        property.first_image = PropertyImage.objects.filter(property=property.property).first()

    context = {
        'last_properties': last_properties,
        'highlighted_properties': highlighted_properties,
    }
    
    return render(request, 'templates/pages/home.html', context)

def property_detail_template(request, slug):
    api_url = f'http://127.0.0.1:8000/api/properties/{slug}/'
    response = requests.get(api_url)
    property_data = response.json() if response.status_code == 200 else None

    context = {
        'property': property_data,
    }

    return render(request, 'templates/pages/property.html', context)

def search_template(request):
    if 'q' in request.GET:
        api_url = f'http://127.0.0.1:8000/api/properties?q={request.GET["q"]}'
        response = requests.get(api_url)
        search_data = response.json() if response.status_code == 200 else None
    else:
        search_data = None
    context = {
        'properties': search_data
    }

    return render(request, 'templates/pages/properties.html', context)

def contact_view(request):
    context = {}
    return render(request, 'templates/pages/contact.html', context)
