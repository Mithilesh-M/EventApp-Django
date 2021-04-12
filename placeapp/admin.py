from .models import Location, Place, City
from django.contrib.gis import admin

admin.site.register(Location, admin.OSMGeoAdmin)
admin.site.register(Place)
admin.site.register(City)
