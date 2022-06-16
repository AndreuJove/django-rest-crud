from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class FlightViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_fail_http_methods(self):
        url = reverse("api:flight", args=["425ba13d-4834-43f2-86d7-301823724b10"])

        # GET
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 400)
        self.assertEqual(
            get_response.json(),
            {
                "message": "Unable to delete the flight with id: 425ba13d-4834-43f2-86d7-301823724b10 because doesn't exist."
            },
        )

        # POST
        post_response = self.client.post(url, data={"paco": 1, "manufacturer": "first"})
        self.assertEqual(post_response.status_code, 405)

        # PUT
        put_response = self.client.put(url, data={"manufacturer": "second"})
        self.assertEqual(put_response.status_code, 400)

        # DELETE
        get_response = self.client.delete(url)
        self.assertEqual(get_response.status_code, 400)

    def test_http_methods_success(self):
        url_post = reverse("api:flights")
        # POST
        post_response = self.client.post(
            url_post,
            data={
                "departure_airport": "dep_airport_1",
                "departure_timestamp": "2022-06-16T21:10:36.091024Z",
                "arrival_airport": "arrival_airport_1",
            },
        )
        self.assertEqual(post_response.status_code, 201)

        # GET list view
        list_view_response = self.client.get(url_post)
        self.assertEqual(len(list_view_response.json()), 1)
        flight_instance = list_view_response.json()[0]
        self.assertEqual(flight_instance["arrival_timestamp"], None)
        self.assertEqual(flight_instance["assigned_to"], None)

        uuid_created = list_view_response.json()[0]["id"]

        # GET detail view
        url = reverse("api:flight", args=[uuid_created])
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 200)

        url_post_aircrafts = reverse("api:aircrafts")
        # POST
        post_response = self.client.post(
            url_post_aircrafts, data={"serial_number": 1, "manufacturer": "one"}
        )

        # PUT
        put_response = self.client.put(
            url,
            data={
                "arrival_timestamp": "2022-06-15T21:10:36.091024Z",
                "aircraft_serial_number": 1,
            },
        )
        self.assertEqual(put_response.status_code, 201)
        list_view_response = self.client.get(url_post)
        self.assertEqual(
            list_view_response.json()[0]["arrival_timestamp"],
            "2022-06-15T21:10:36.091024Z",
        )
        self.assertEqual(list_view_response.json()[0]["assigned_to"], 1)

        # DELETE
        delete_response = self.client.delete(url)
        self.assertEqual(delete_response.status_code, 200)
        list_view_response = self.client.get(url_post)
        self.assertEqual(len(list_view_response.json()), 0)
