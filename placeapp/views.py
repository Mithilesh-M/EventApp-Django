from django.shortcuts import render
from .models import Location, Place, City
from eventapp.models import Event, Timing
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateCityForm, CreatePlaceForm, UpdateCityForm, UpdatePlaceForm
from django.contrib.auth.decorators import login_required, permission_required
import datetime


def index(request):
    """View function for home page of site."""

    num_places = Place.objects.all().count()
    num_cities = City.objects.all().count()
    total_events = Event.objects.all().count()
    date = datetime.date.today()
    num_upcoming = Timing.objects.filter(date__gte=date).count()

    context = {
        'num_places': num_places,
        'num_cities': num_cities,
        'total_events': total_events,
        'num_upcoming': num_upcoming,
    }

    return render(request, 'index.html', context=context)


class CityListView(generic.ListView):
    model = City
    paginate_by = 10


class PlaceListView(generic.ListView):
    model = Place
    paginate_by = 10


class CityDetailView(generic.DetailView):
    model = City
    paginate_by = 10


class PlaceDetailView(generic.DetailView):
    model = Place
    paginate_by = 10


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def CreateCity(request):
    """View function for Creating city."""

    if request.method == 'POST':

        form = CreateCityForm(request.POST)

        if form.is_valid():
            city = City(name=form.cleaned_data['name'])
            city.save()

            return HttpResponseRedirect(reverse('cities') )

    else:
        form = CreateCityForm()

    context = {
        'form': form,
    }

    return render(request, 'placeapp/create_city.html', context)


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def CreatePlace(request):
    """View function for Creating Place."""

    if request.method == 'POST':

        form = CreatePlaceForm(request.POST)

        if form.is_valid():
            place = Place(title=form.cleaned_data['title'],description=form.cleaned_data['description'],address=form.cleaned_data['address'],phone=form.cleaned_data['phone'],city=form.cleaned_data['city'],type_of_place=form.cleaned_data['type_of_place'],)
            place.save()

            return HttpResponseRedirect(reverse('places'))

    else:
        form = CreatePlaceForm()

    context = {
        'form': form,
    }

    return render(request, 'placeapp/create_place.html', context)


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def PlaceDelete(request, pk):
    """View function for deleting the place."""
    place = get_object_or_404(Place, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        place.delete()
        return HttpResponseRedirect(reverse('places'))

    context = {
        'place': place,
    }

    return render(request, 'placeapp/delete_place.html', context)


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def CityDelete(request, pk):
    """View function for deleting the city."""
    city = get_object_or_404(City, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        city.delete()
        return HttpResponseRedirect(reverse('places'))

    context = {
        'city': city,
    }

    return render(request, 'placeapp/delete_city.html', context)


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def CityUpdate(request, pk):
    """View function for updating city."""
    city = get_object_or_404(City, pk=pk)

    if request.method == 'POST':

        form = UpdateCityForm(request.POST)

        if form.is_valid():
            city.name = form.cleaned_data['name']
            city.save()
            return HttpResponseRedirect(reverse('cities'))

    else:
        city_original_name = city.name
        form = UpdateCityForm(initial={'name': city_original_name})

    context = {
        'form': form,
        'city': city,
    }

    return render(request, 'placeapp/update_city.html', context)


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def PlaceUpdate(request, pk):
    """View function for updating Place."""
    place = get_object_or_404(Place, pk=pk)

    if request.method == 'POST':

        form = UpdatePlaceForm(request.POST)

        if form.is_valid():
            place.title = form.cleaned_data['title']
            place.description = form.cleaned_data['description']
            place.address = form.cleaned_data['address']
            place.phone = form.cleaned_data['phone']
            place.city = form.cleaned_data['city']
            place.type_of_place = form.cleaned_data['type_of_place']
            place.save()
            return HttpResponseRedirect(reverse('places'))

    else:
        place_original_title = place.title
        place_original_description = place.description
        place_original_address = place.address
        place_original_phone = place.phone
        place_original_city = place.city
        place_original_type_of_place = place.type_of_place
        form = UpdatePlaceForm(initial={'title': place_original_title,'description':place_original_description,'address':place_original_address,'phone':place_original_phone,'city':place_original_city,'type_of_place':place_original_type_of_place})

    context = {
        'form': form,
        'place': place,
    }

    return render(request, 'placeapp/update_place.html', context)
