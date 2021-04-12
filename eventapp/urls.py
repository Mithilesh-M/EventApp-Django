from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('event/create/', views.CreateEvent, name='create-event'),
]