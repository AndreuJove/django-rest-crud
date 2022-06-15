from typing import Optional

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Flight
from api.serializers import FlightInputSerializer, FlightOutputSerializer

# from api.services.aircraft_service import AircraftService


def get_flight_by_id(id: str) -> Optional[Flight]:
    try:
        result = Flight.objects.get(id=id)
    except Flight.DoesNotExist:
        result = None
    return result


class FlightView(APIView):
    def delete(self, request, id, *args, **kwargs):
        flight_instance = get_flight_by_id(id)

        if not flight_instance:
            return Response(
                {
                    "message": f"Unable to delete the flight with id: {id} because doesn't exist."
                },
                status=status.HTTP_400_OK,
            )

        flight_instance.delete()
        return Response({"message": "Object deleted"}, status=status.HTTP_200_OK)


class FlightListView(APIView):
    def get(self, request, *args, **kwargs):
        # aircrafts = AircraftService.get_all_aircrafts()
        flights = Flight.objects.all()

        departure_airport = self.request.query_params.get("departure_airport")
        arrival_airport = self.request.query_params.get("arrival_airport")
        start_time = self.request.query_params.get("start_time")
        end_time = self.request.query_params.get("end_time")

        if departure_airport:
            flights = flights.filter(departure_airport=departure_airport)

        if arrival_airport:
            flights = flights.filter(arrival_airport=arrival_airport)

        if start_time and end_time:
            flights = flights.filter(departure_timestamp__range=(start_time, end_time))

        serializer = FlightOutputSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        # aircraft_serial_number = request.data.get("aircraft_serial_number")
        # aircraft_instance = AircraftService.get_aircraft_by_serial_number(
        #     "aircraft_serial_number"
        # )
        # if aircraft_serial_number and not aircraft_instance:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        data = {
            "departure_airport": request.data.get("departure_airport"),
            "departure_timestamp": request.data.get("departure_timestamp"),
            "arrival_airport": request.data.get("arrival_airport"),
            # "aircraft": aircraft_instance,
        }
        serializer = FlightInputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
