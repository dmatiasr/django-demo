from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils import timezone


class Property(models.Model):
    '''
     represent a Property
    '''
    PROPERTY_TYPE = (('house', 'house'), ('departament', 'departament'), ('local', 'local'), ('camping', 'camping'))
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=3000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    lat = models.CharField(max_length=30, null=True)
    lon = models.CharField(max_length=30, null=True)
    location_point = models.PointField(default='POINT( 0.0 0.0 )', srid=4326,
                                       help_text="Represented as (longitude, latitude)")
    type = models.CharField(choices=PROPERTY_TYPE, null=True, max_length=50, blank=True)
    related_sector = models.ForeignKey('UrbanizedSector', null=True, on_delete=models.SET_NULL)
    available = models.BooleanField(default=True)
    objects = models.GeoManager()
    updated_at = models.DateTimeField(null=True, blank=True, default=timezone.now, verbose_name='property_updated_at')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='property_updated_by')
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now, verbose_name='property_created_at' )
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='property_created_by')


class UrbanizedSector(models.Model):
    '''
        represent a Polygon that contain all possible urbanized sectors.
    '''
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    polygon_representation = models.PolygonField(srid=4326,
                                                 help_text='POLYGON((lon lat, lon lat, lon lat, lon lat, lon lat))')
    updated_at = models.DateTimeField(null=True, blank=True, default=timezone.now, verbose_name='urbanized_sector_updated_at')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='urbanized_sector_updated_by')
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now, verbose_name='urbanized_sector_created_at')
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='urbanized_sector_created_by')
    objects = models.GeoManager()

# TO-DO agregar popularidad por cada propiedad. entity