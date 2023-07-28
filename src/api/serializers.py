from rest_framework import serializers
from whimsi.models import Property, PropertyAddress

class PropertyAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    address = PropertyAdressSerializer(source='propertyaddress', read_only=True)

    class Meta:
        model = Property
        fields = '__all__'
