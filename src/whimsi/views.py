from django.shortcuts import render
from .models import HighlightedProperty

def home_view(request):
    highlighted_properties = HighlightedProperty.objects.prefetch_related('property__propertyaddress').all()

    context = {
        'highlighted_properties': highlighted_properties,
    }
    
    return render(request, 'templates/pages/home.html', context)