from django.urls import path
from . views import home_view, property_detail_template, search_template

urlpatterns = [
    path('', home_view, name='home'),
    path('properties/', search_template, name='search-template'),
    path('properties/<slug:slug>/', property_detail_template, name='property-detail-template'),
]