from api.models import Aircraft


class AircraftService:
    def __init__(self):
        pass

    @classmethod
    def get_all_aircrafts(cls):
        return Aircraft.objects.all()

    @classmethod
    def get_aircraft_by_serial_number(cls, serial_number: str):
        try:
            result = Aircraft.objects.get(serial_number=serial_number)
        except Aircraft.DoesNotExist:
            result = None
        return result
