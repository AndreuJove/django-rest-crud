from rest_framework import serializers

from .models import Aircraft, Flight


class AircraftSerializer(serializers.ModelSerializer):
    flights = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Aircraft
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


"""

{"departure_airport": "dep_airport_3",
"departure_timestamp": "2022-06-16T21:10:36.091024Z",
"arrival_airport": "arrival_airport_3",
"aircraft":     {
        "serial_number": 12323121,
        "manufacturer": "asdas1asdasa"
    }
}



{"departure_airport": "dep_airport_3",
"departure_timestamp": "2022-06-16T21:10:36.091024Z",
"arrival_airport": "arrival_airport_3",
"aircraft_serial_number": 12323121
}

"""
