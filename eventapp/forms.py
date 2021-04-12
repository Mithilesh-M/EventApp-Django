from taggit import forms as tags
from django import forms
from placeapp.models import Place
from django.contrib.auth.models import User


class CreateEventForm(forms.Form):
    title = forms.CharField(max_length=200, help_text="Enter the name of the event")
    place = forms.ModelChoiceField(queryset=Place.objects.all())
    description = forms.CharField(max_length=200, help_text="Enter the description of the event")
    user = forms.ModelChoiceField(queryset=User.objects.all())
    tags = tags.TagField()

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data
