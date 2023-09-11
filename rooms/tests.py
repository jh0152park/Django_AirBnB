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


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESCRIPTION = "TEST Description"

    def setUp(self):
        Amenity.objects.create(
            name=self.NAME,
            description=self.DESCRIPTION,
        )

    def test_amenity_not_found(self):
        res = self.client.get("/api/v1/rooms/amenities/10")
        self.assertEqual(res.status_code, 404)

    def test_get_amenity(self):
        res = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(res.status_code, 200)

        data = res.json()

        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESCRIPTION,
        )

    # create put test code is my challenge
    def test_put_amenity(self):
        res = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(
            res.status_code,
            200,
            "status code is not 200 at test put code",
        )

        data = res.json()
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESCRIPTION,
        )

        res = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": self.NAME,
            },
        )
        data = res.json()
        self.assertEqual(
            res.status_code,
            200,
            "status code is not 200 at name put",
        )
        self.assertEqual(
            data["name"],
            self.NAME,
        )

        res = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "description": self.DESCRIPTION,
            },
        )
        data = res.json()
        self.assertEqual(
            res.status_code,
            200,
            "status code is not 200 at name put",
        )
        self.assertEqual(
            data["description"],
            self.DESCRIPTION,
        )

    def test_delete_amenity(self):
        res = self.client.delete("/api/v1/rooms/amenities/1")
        self.assertEqual(
            res.status_code,
            204,
            "status code of delete amenity is not a 204",
        )
