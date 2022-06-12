from api.serializers import AircraftSerializer
from api.services.aircraft_service import AircraftService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AircraftView(APIView):
    @staticmethod
    def return_bad_request(serial_number: str):
        return Response(
            {
                "message": f"Aircraft with the serial_number {serial_number} does not exists"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, serial_number, *args, **kwargs):
        aircraft_instance = AircraftService.get_aircraft_by_serial_number(serial_number)
        if not aircraft_instance:
            return self.return_bad_request(serial_number)

        serializer = AircraftSerializer(aircraft_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, serial_number, *args, **kwargs):
        aircraft_instance = AircraftService.get_aircraft_by_serial_number(serial_number)

        if not aircraft_instance:
            return self.return_bad_request(serial_number)

        data = {
            "manufacturer": request.data.get("manufacturer"),
        }
        serializer = AircraftSerializer(
            instance=aircraft_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, serial_number, *args, **kwargs):
        aircraft_instance = AircraftService.get_aircraft_by_serial_number(serial_number)

        if not aircraft_instance:
            return self.return_bad_request(serial_number)

        aircraft_instance.delete()
        return Response({"message": "Object deleted"}, status=status.HTTP_200_OK)


class AircraftListView(APIView):
    def get(self, request, *args, **kwargs):
        aircrafts = AircraftService.get_all_aircrafts()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "serial_number": request.data.get("serial_number"),
            "manufacturer": request.data.get("manufacturer"),
        }
        serializer = AircraftSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
