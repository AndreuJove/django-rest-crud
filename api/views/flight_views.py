from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import FlightSerializer
from api.services.aircraft_service import AircraftService
from api.services.flight_service import FlightService


class FlightView(APIView):
    def get(self, request, flight_id, *args, **kwargs):
        flight_instance = FlightService.get_flight_by_id(flight_id)
        if not flight_instance:
            return Response(
                {
                    "message": f"Unable to delete the flight with id: {flight_id} because doesn't exist."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = FlightSerializer(flight_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, flight_id, *args, **kwargs):
        flight_instance = FlightService.get_flight_by_id(flight_id)

        if not flight_instance:
            return Response(
                {
                    "message": f"Unable to delete the flight with id: {flight_id} because doesn't exist."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        aircraft_serial_number = request.data.get("aircraft_serial_number")
        aircraft_instance = AircraftService.get_aircraft_by_serial_number(
            aircraft_serial_number
        )

        if aircraft_serial_number and not aircraft_instance:
            return Response(
                {
                    "message": "There is no aircraft with the aircraft_serial_number provided"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "arrival_timestamp": request.data.get("arrival_timestamp"),
        }

        serializer = FlightSerializer(instance=flight_instance, data=data, partial=True)
        if serializer.is_valid():
            if aircraft_instance:
                serializer.save(assigned_to=aircraft_instance)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request, flight_id, *args, **kwargs):
        flight_instance = FlightService.get_flight_by_id(flight_id)

        if not flight_instance:
            return Response(
                {
                    "message": f"Unable to delete the flight with id: {flight_id} because doesn't exist."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        flight_instance.delete()
        return Response({"message": "Object deleted"}, status=status.HTTP_200_OK)


class FlightListView(APIView):
    def get(self, request, *args, **kwargs):
        flights = FlightService.get_all_flights()

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

        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        aircraft_serial_number = request.data.get("aircraft_serial_number")
        aircraft_instance = AircraftService.get_aircraft_by_serial_number(
            aircraft_serial_number
        )

        if aircraft_serial_number and not aircraft_instance:
            return Response(
                {
                    "message": "There is no aircraft with the aircraft_serial_number provided"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "departure_airport": request.data.get("departure_airport"),
            "departure_timestamp": request.data.get("departure_timestamp"),
            "arrival_airport": request.data.get("arrival_airport"),
        }
        serializer = FlightSerializer(data=data)
        if serializer.is_valid():
            serializer.save(assigned_to=aircraft_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
