from django.urls import path
from . views import home_view, property_view

urlpatterns = [
    path('', view=home_view, name='home'),
    path('property/', view=property_view, name='property_details'),
]