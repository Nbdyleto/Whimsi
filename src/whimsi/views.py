from django.shortcuts import render
from .models import Property, HighlightedProperty

def home_view(request):
    last_properties = Property.objects.order_by('-created_at')[:3]
    print('last_properties', last_properties)
    highlighted_properties = HighlightedProperty.objects.prefetch_related('property__propertyaddress').all()

    context = {
        'last_properties': last_properties,
        'highlighted_properties': highlighted_properties,
    }
    
    return render(request, 'templates/pages/home.html', context)

def property_view(request):
    return render(request, 'templates/pages/property.html', {})