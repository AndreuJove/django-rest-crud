from rest_framework import serializers

from .models import Aircraft, Flight


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = [
            "serial_number",
            "manufacturer",
        ]


class FlightOutputSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer(required=False, read_only=True)

    class Meta:
        model = Flight
        fields = [
            "id",
            "aircraft",
            "departure_airport",
            "departure_timestamp",
            "arrival_airport",
            "arrival_timestamp",
        ]

    # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     if data['departure_airport'] > data['arrival_timestamp']:
    #         raise serializers.ValidationError({"end_date": "finish must occur after start"})
    #     return data


class FlightInputSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer(required=False, read_only=True)

    class Meta:
        model = Flight
        fields = [
            "aircraft",
            "departure_airport",
            "departure_timestamp",
            "arrival_airport",
        ]
