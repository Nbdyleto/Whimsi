from django.urls import path, include
from . views import home_view, property_detail_template

urlpatterns = [
    path('', home_view, name='home'),
    path('properties/<slug:slug>/', property_detail_template, name='property-detail-template'),
]