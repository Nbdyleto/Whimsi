from django import forms
from .models import PropertyRegion

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=254)
    phone = forms.CharField(label='Telefone', max_length=11)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)
    agree_privacy = forms.BooleanField(label='Estou de acordo com a política de privacidade')

class FilterForm(forms.Form):
    REG_CHOICES = [('', ''),]
    region_names = PropertyRegion.objects.values_list('region_name', flat=True).distinct()
    REG_CHOICES.extend([(region_name, region_name) for region_name in region_names])
    
    region = forms.ChoiceField(choices=REG_CHOICES, required=False)
    
    BEDROOM_CHOICES = (('', ''), 
                    ('1', '1 Dorms.'), ('2', '2 Dorms.'), 
                    ('3', '3 Dorms.'), ('4', '4 Dorms.'),)
    bedrooms = forms.ChoiceField(choices=BEDROOM_CHOICES, required=False)

    TYPE_CHOICES = (('', ''), ('Apartamento', 'Apartamento'), ('Casa', 'Casa'),)
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False)

    VALUE_CHOICES = (('', ''), 
                     ('100000', '100.000,00'), ('200000', '200.000,00'), ('300000', '300.000,00'), 
                     ('400000', '400.000,00'), ('500000', '500.000,00'), ('600000', '600.000,00'), 
                     ('700000', '700.000,00'), ('800000', '800.000,00'), ('900000', '900.000,00'),
                     ('1000000', '1.000.000,00'),)
    max_value = forms.ChoiceField(choices=VALUE_CHOICES, required=False)
