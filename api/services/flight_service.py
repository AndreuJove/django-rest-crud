from api.models import Flight


class FlightService:
    def __init__(self):
        pass

    @classmethod
    def get_all_flights(cls):
        return Flight.objects.all()

    @classmethod
    def get_flight_by_id(cls, flight_id: str):
        try:
            result = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            result = None
        return result
