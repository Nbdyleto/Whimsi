from django.urls import path
from .views import PropertyDetailView, SearchResultsListView

urlpatterns = [
    path('properties/<slug:slug>/', PropertyDetailView.as_view(), name='property-detail'),
    path('properties/', SearchResultsListView.as_view(), name='search')
]