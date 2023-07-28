from django.urls import path, include
from . views import home_view, properties_template, property_detail_template

urlpatterns = [
    path('', home_view, name='home'),
    path('properties/', properties_template, name='properties-template'),
    path('properties/<slug:slug>/', property_detail_template, name='property-detail-template'),
]