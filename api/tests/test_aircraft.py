from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class AircraftViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_fail_http_methods(self):
        url = reverse("api:aircraft", args=[1])

        # GET
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 400)

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
        url = reverse("api:aircraft", args=[2])

        url_post = reverse("api:aircrafts")
        # POST
        post_response = self.client.post(
            url_post, data={"serial_number": 2, "manufacturer": "one"}
        )

        self.assertEqual(post_response.status_code, 201)

        # GET list view
        list_view_response = self.client.get(url_post)
        self.assertEqual(len(list_view_response.json()), 1)

        # GET detail view
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 200)

        # PUT
        put_response = self.client.put(url, data={"manufacturer": "two"})
        self.assertEqual(put_response.status_code, 201)
        list_view_response = self.client.get(url_post)
        self.assertEqual(list_view_response.json()[0]["manufacturer"], "two")

        # DELETE
        delete_response = self.client.delete(url)
        self.assertEqual(delete_response.status_code, 200)
        list_view_response = self.client.get(url_post)
        self.assertEqual(len(list_view_response.json()), 0)
