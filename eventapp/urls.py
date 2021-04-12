from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view(), name='events'),
]