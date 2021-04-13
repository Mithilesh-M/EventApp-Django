from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cities/', views.CityListView.as_view(), name='cities'),
    path('places/', views.PlaceListView.as_view(), name='places'),
    path('city/<int:pk>', views.CityDetailView.as_view(), name='city-detail'),
    path('place/<int:pk>', views.PlaceDetailView.as_view(), name='place-detail'),
    path('city/create/', views.CreateCity, name='create-city'),
    path('place/create/', views.CreatePlace, name='create-place'),
    path('place/<int:pk>/delete', views.PlaceDelete, name='place-delete'),
    path('city/<int:pk>/delete', views.CityDelete, name='city-delete'),
    path('city/<int:pk>/update', views.CityUpdate, name='city-update'),
    path('place/<int:pk>/update', views.PlaceUpdate, name='place-update'),
    path('place/<int:pk>/map', views.PlaceMap, name='place-map'),
]