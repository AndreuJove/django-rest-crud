from django.urls import path

from .views.aircraft_views import AircraftListView, AircraftView

app_name = "api"

urlpatterns = [
    path(
        "aircraft/<serial_number>/",
        AircraftView.as_view(),
        name="aircraft",
    ),
    path("aircraft/", AircraftListView.as_view(), name="aircrafts"),
]
