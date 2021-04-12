from django.db import models
from django.contrib.gis.db import models as geomodels
from django.urls import reverse


class Place(models.Model):
    """Model representing a place."""
    title = models.CharField(max_length=100, help_text='Enter a place name')
    location = models.OneToOneField('Location', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=500, help_text='Enter a place description')
    address = models.CharField(max_length=250, help_text='Enter a place address')
    phone = models.CharField(max_length=10, help_text='Enter a phone number')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)
    PLACE_TYPE = (
        ('a', 'Park'),
        ('b', 'Restaurant'),
        ('c', 'Mall'),
        ('d', 'Amusement park'),
        ('e', 'Museum'),
        ('f', 'Beach'),
        ('g', 'Theater'),
        ('h', 'Lodge'),
        ('i', 'Others'),
    )
    type_of_place = models.CharField(
        max_length=1,
        choices=PLACE_TYPE,
        blank=False,
        default='m',
        help_text='Place Type',
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular place instance."""
        return reverse('place-detail', args=[str(self.id)])


class City(models.Model):
    """Model representing a city."""
    name = models.CharField(max_length=100, help_text='Enter a city name', null=False, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular city instance."""
        return reverse('city-detail', args=[str(self.id)])


class Location(geomodels.Model):
    """Model representing a location."""
    name = models.CharField(max_length=100, help_text='Enter a place name',null=False, blank=False)
    point = geomodels.PointField(
        srid=4326,
        blank=True,
        )

    def __str__(self):
        """String for representing the Model object."""
        return self.name