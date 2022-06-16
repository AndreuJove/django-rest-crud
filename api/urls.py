from django.urls import path

from api.views.aircraft_views import AircraftListView, AircraftView
from api.views.flight_views import FlightListView, FlightView

app_name = "api"

urlpatterns = [
    path(
        "aircraft/<serial_number>/",
        AircraftView.as_view(),
        name="aircraft",
    ),
    path("aircraft/", AircraftListView.as_view(), name="aircrafts"),
    path("flight/", FlightListView.as_view(), name="flights"),
    path(
        "flight/<flight_id>/",
        FlightView.as_view(),
        name="flight",
    ),
]
