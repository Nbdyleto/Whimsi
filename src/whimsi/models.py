from django.db import models
from django.utils.text import slugify

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    parking_lots = models.PositiveIntegerField(null=True, blank=True, default=0)
    area_sqm = models.PositiveIntegerField()
    STATUS_CHOICES = (
        ('Comprar', 'Comprar'),
        ('Alugar', 'Alugar'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    TYPE_CHOICES = (
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class PropertyRegion(models.Model):
    REGION_CHOICES = (
        ('Zona Sul', 'Zona Sul'),
        ('Zona Norte', 'Zona Norte'),
        ('Zona Leste', 'Zona Leste'),
        ('Zona Oeste', 'Zona Oeste'),
    )

    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=100, choices=REGION_CHOICES)

    def __str__(self):
        return self.get_region_name_display()

class PropertyAddress(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    street_address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=8)
    region = models.ForeignKey(PropertyRegion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.property.title} - {self.postal_code}, {self.street_address}, {self.neighborhood}, {self.city}'

class PropertyImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return 'img ' + self.property.title

class PropertyFeature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=255)

class HighlightedProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    highlight_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property.title