from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from placeapp.models import Place

class Event(models.Model):
    """Model representing a Event."""
    title = models.CharField(max_length=200, help_text='Enter a event name')
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager()
    description = models.CharField(max_length=200, help_text='Enter a event description')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    modified = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Timing(models.Model):
    """Model representing a Timing."""
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True, blank=True)
    timing = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
