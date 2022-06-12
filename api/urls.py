from django.urls import path

from .views import AircraftListView, AircraftView

urlpatterns = [
    path(
        "api/<serial_number>/",
        AircraftView.as_view(),
        name="aircraft",
    ),
    path("api/", AircraftListView.as_view()),
]
