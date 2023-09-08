from rest_framework.test import APITestCase

from .models import Amenity


class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESCRIPTION = "Amenity Test"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        Amenity.objects.create(
            name=self.NAME,
            description=self.DESCRIPTION,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code is not 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESCRIPTION,
        )

    def test_create_amenity(self):
        response = self.client.get(
            self.URL,
            data={
                "name": self.NAME,
                "description": self.DESCRIPTION,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code is not 200.",
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESCRIPTION,
        )

        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)
