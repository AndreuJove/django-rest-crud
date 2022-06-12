from django.urls import path

from .views.views import AircraftListView, AircraftView

app_name = "api"

urlpatterns = [
    path(
        "api/<serial_number>/",
        AircraftView.as_view(),
        name="aircraft",
    ),
    path("api/", AircraftListView.as_view(), name="aircrafts"),
]
