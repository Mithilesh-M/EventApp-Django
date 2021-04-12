from django.shortcuts import render
from django.views import generic
from .models import Event, Timing
from .forms import CreateEventForm
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
