from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('event/create/', views.CreateEvent, name='create-event'),
    path('event/<int:pk>/delete', views.EventDelete, name='event-delete'),
    path('event/<int:pk>/update', views.EventUpdate, name='event-update'),
    path('event/<int:pk>/addtime/', views.AddTime, name='add-event-time'),
    path('event/<int:pk>/deletetime/', views.DeleteTime, name='delete-event-time'),
]