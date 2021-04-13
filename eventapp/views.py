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
            tags = form.cleaned_data['tags']
            event = Event(title=form.cleaned_data['title'], place=form.cleaned_data['place'], description=form.cleaned_data['description'], user=form.cleaned_data['user'])
            event.save()
            for tag in tags:
                event.tags.add(tag)

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
        return HttpResponseRedirect(reverse('events'))

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
            tags = form.cleaned_data['tags']
            event.title = form.cleaned_data['title']
            event.place = form.cleaned_data['place']
            event.description = form.cleaned_data['description']
            event.user = form.cleaned_data['user']
            event.save()
            event.tags.clear()
            for tag in tags:
                event.tags.add(tag)
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

def DeleteTime(request, pk):
    """View function for deleting the city."""
    time = get_object_or_404(Timing, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        time.delete()
        return HttpResponseRedirect(reverse('events'))

    context = {
        'time': time,
    }

    return render(request, 'eventapp/time_deleteform.html', context)

def FilterEvent(request):
    """View function for filtering events."""

    today_year = datetime.date.today().year
    today_month = datetime.date.today().month
    today_day = datetime.date.today().day
    date = datetime.datetime.now()+datetime.timedelta(days=1)
    today = Timing.objects.filter(date=datetime.date(today_year,today_month,today_day))
    tomorrow = Timing.objects.filter(date=datetime.date(date.year,date.month,date.day))
    timedelta = datetime.datetime.now()+datetime.timedelta(days=1)
    start_date = datetime.date.today()
    kwargs = {}
    kwargs['day'] = int(timedelta.day)
    kwargs['month'] = int(timedelta.month)
    kwargs['year'] = int(timedelta.year)
    start_date = start_date.replace(**kwargs)
    timedelta = datetime.datetime.now()+datetime.timedelta(days=8)
    end_date = datetime.date.today()
    kwargs = {}
    kwargs['day'] = int(timedelta.day)
    kwargs['month'] = int(timedelta.month)
    kwargs['year'] = int(timedelta.year)
    end_date = end_date.replace(**kwargs)
    week = Timing.objects.filter(date__range=[start_date, end_date])
    timedelta = datetime.datetime.now() + datetime.timedelta(days=30)
    end_date = datetime.date.today()
    kwargs = {}
    kwargs['day'] = int(timedelta.day)
    kwargs['month'] = int(timedelta.month)
    kwargs['year'] = int(timedelta.year)
    end_date = end_date.replace(**kwargs)
    month = Timing.objects.filter(date__range=[start_date, end_date])
    timedelta = datetime.datetime.now() + datetime.timedelta(days=365)
    end_date = datetime.date.today()
    kwargs = {}
    kwargs['day'] = int(timedelta.day)
    kwargs['month'] = int(timedelta.month)
    kwargs['year'] = int(timedelta.year)
    end_date = end_date.replace(**kwargs)
    year = Timing.objects.filter(date__range=[start_date, end_date])

    context = {
        'today': today,
        'tomorrow': tomorrow,
        'week': week,
        'month': month,
        'year': year,
    }

    return render(request, 'eventapp/filter_events.html', context=context)
