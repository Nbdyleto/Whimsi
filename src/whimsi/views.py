import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import Property, HighlightedProperty, PropertyImage

def home_view(request):
    last_properties = Property.objects.order_by('-created_at')[:3]
    for property in last_properties:
        property.first_image = PropertyImage.objects.filter(property=property).first()
    
    highlighted_properties = HighlightedProperty.objects.prefetch_related('property__propertyaddress').all()
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            agree_privacy = form.cleaned_data['agree_privacy']
            content = f'{name} - Telefone: {phone} \n\n {message}'

            EmailMessage(
                f'Contact form from {name}',
                content,
                f'{email}', # from 
                ['nobodyleto2004@protonmail.com'],
                reply_to=[email]
            ).send()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    context = {'form': form}
    
    return render(request, 'templates/pages/contact.html', context)
