from django.urls import path
from . views import home_view

urlpatterns = [
    path('', view=home_view, name='home'),
]