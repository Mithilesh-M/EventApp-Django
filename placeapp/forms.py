import datetime

from django import forms
from django.contrib.gis import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Location, Place, City

class CreateCityForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter the name of the city")

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data

class CreatePlaceForm(forms.Form):
    title = forms.CharField(max_length=100, help_text='Enter a place name')
    #location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    description = forms.CharField(max_length=500, help_text='Enter a place description')
    address = forms.CharField(max_length=250, help_text='Enter a place address')
    phone = forms.CharField(max_length=10, help_text='Enter a phone number')
    city = forms.ModelChoiceField(queryset=City.objects.all())
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
    type_of_place = forms.ChoiceField(
        choices=PLACE_TYPE,
        help_text='Place Type',
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data


class UpdateCityForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter the name of the city")

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data

class UpdatePlaceForm(forms.Form):
    title = forms.CharField(max_length=100, help_text='Enter a place name')
    # location = forms.ModelChoiceField(queryset=Location.objects.all())
    description = forms.CharField(max_length=500, help_text='Enter a place description')
    address = forms.CharField(max_length=250, help_text='Enter a place address')
    phone = forms.CharField(max_length=10, help_text='Enter a phone number')
    city = forms.ModelChoiceField(queryset=City.objects.all())
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
    type_of_place = forms.ChoiceField(
        choices=PLACE_TYPE,
        help_text='Place Type',
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data
