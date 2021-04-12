from django.shortcuts import render
from django.views import generic
from .models import Event, Timing

class EventListView(generic.ListView):
    model = Event
    paginate_by = 10

class EventDetailView(generic.DetailView):
    model = Event
    paginate_by = 10
