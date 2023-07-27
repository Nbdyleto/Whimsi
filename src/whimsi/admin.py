from django.contrib import admin
from .models import Property, PropertyAddress, PropertyFeature, PropertyImage, HighlightedProperty

admin.site.register(Property)
admin.site.register(PropertyAddress)
admin.site.register(PropertyFeature)
admin.site.register(PropertyImage)
admin.site.register(HighlightedProperty)