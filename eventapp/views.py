from django.shortcuts import render
from django.views import generic
from .models import Event, Timing
from .forms import CreateEventForm, UpdateEventForm, AddTimeForm
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import get_object_or_404


class EventListView(generic.ListView):
    model = Event
    paginate_by = 10


class EventDetailView(generic.DetailView):
    model = Event
    paginate_by = 10


def CreateEvent(request):
    """View function for Creating Event."""

    if request.method == 'POST':

        form = CreateEventForm(request.POST)

        if form.is_valid():
            date= datetime.date.today()
            event = Event(title=form.cleaned_data['title'], place=form.cleaned_data['place'], description=form.cleaned_data['description'], tags=form.cleaned_data['tags'], user=form.cleaned_data['user'], created=date, modified=date)
            event.save()

            return HttpResponseRedirect(reverse('events'))

    else:
        form = CreateEventForm()

    context = {
        'form': form,
    }

    return render(request, 'eventapp/create_event.html', context)


def EventDelete(request, pk):
    """View function for deleting the city."""
    event = get_object_or_404(Event, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        event.delete()
        return HttpResponseRedirect(reverse('places'))

    context = {
        'event': event,
    }

    return render(request, 'eventapp/delete_event.html', context)

def EventUpdate(request, pk):
    """View function for updating event."""
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':

        form = UpdateEventForm(request.POST)

        if form.is_valid():
            event.title = form.cleaned_data['title']
            event.place = form.cleaned_data['place']
            event.description = form.cleaned_data['description']
            event.user = form.cleaned_data['user']
            event.tags = form.cleaned_data['tags']
            event.modified = datetime.date.today()
            event.save()
            return HttpResponseRedirect(reverse('events'))

    else:
        event_original_title = event.title
        event_original_place = event.place
        event_original_description = event.description
        event_original_user = event.user
        event_original_tags = event.tags.all()
        form = UpdateEventForm(initial={'title': event_original_title,'place': event_original_place, 'description':event_original_description, 'user':event_original_user, 'tags':event_original_tags})

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'eventapp/update_event.html', context)

def AddTime(request, pk):
    """View function for adding timing to event."""

    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':

        form = AddTimeForm(request.POST)

        if form.is_valid():
            event.timing_set.create(timing=form.cleaned_data['timing'],date=form.cleaned_data['date'])
            return HttpResponseRedirect(reverse('event-detail', args=(event.id,) ))

    else:
        form = AddTimeForm()

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'eventapp/time_createform.html', context)
