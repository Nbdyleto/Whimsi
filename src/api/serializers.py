from rest_framework import serializers
from whimsi.models import Property, PropertyAddress, PropertyImage

class PropertyAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    address = PropertyAdressSerializer(source='propertyaddress', read_only=True)
    property_images = PropertyImageSerializer(source='propertyimage_set', many=True,read_only=True)
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'

    def get_first_image(self, obj):
        first_image = PropertyImage.objects.filter(property=obj).first()
        if first_image:
            return first_image.image.url
        return None