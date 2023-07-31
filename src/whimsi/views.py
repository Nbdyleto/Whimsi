import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from .forms import ContactForm, FilterForm
from .models import Property, HighlightedProperty, PropertyImage

class HomeFilterForm(FilterForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('bedrooms')

def home_view(request):
    filter_form = HomeFilterForm()

    last_properties = Property.objects.order_by('-created_at')[:3]
    for property in last_properties:
        property.first_image = PropertyImage.objects.filter(property=property).first()
    
    highlighted_properties = HighlightedProperty.objects.prefetch_related('property__propertyaddress').all()
    for property in highlighted_properties:
        property.first_image = PropertyImage.objects.filter(property=property.property).first()

    context = {
        'last_properties': last_properties,
        'highlighted_properties': highlighted_properties,
        'filter_form': filter_form,
    }
    
    return render(request, 'templates/pages/home.html', context)

def property_detail_template(request, slug):
    api_url = f'http://127.0.0.1:8000/api/properties/{slug}/'
    response = requests.get(api_url)
    property_data = response.json() if response.status_code == 200 else None

    contact_form = ContactForm()

    context = {
        'property': property_data,
        'contact_form': contact_form,
    }

    return render(request, 'templates/pages/property.html', context)

def search_template(request):
    if request.method == 'POST':
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            region = filter_form.cleaned_data['region']
            bedrooms = filter_form.cleaned_data['bedrooms']
            type = filter_form.cleaned_data['type']
            max_val = filter_form.cleaned_data['max_value']

            params = {
                'region': region,
                'bedrooms': bedrooms,
                'type': type,
                'max_value': max_val,
            }

            api_url = 'http://127.0.0.1:8000/api/properties/'
            response = requests.get(api_url, params=params)

            if response.status_code == 200:
                properties = response.json()
            else:
                properties = []

            context = {
                'properties': properties,
                'filter_form': filter_form,
            }
            return render(request, 'templates/pages/properties.html', context)
    else:
        api_url = 'http://127.0.0.1:8000/api/properties/'
        params = {}
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            properties = response.json()
        else:
            properties = []

        filter_form = FilterForm()
        
        context = {
            'properties': properties,
            'filter_form': filter_form,
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
