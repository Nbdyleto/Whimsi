from django.urls import path
from .views import PropertyDetailView

urlpatterns = [
    path('properties/<slug:slug>/', PropertyDetailView.as_view(), name='property-detail')
]