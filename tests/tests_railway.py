from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

TICKET_URL = reverse("railway_station:ticket-list")
TRAIN_URL = reverse("railway_station:train-list")

class AuthenticatedTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.client.force_authenticate(user=self.user)

    def test_train_list_authenticated(self):
        res = self.client.get(TRAIN_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_ticket_list_authenticated(self):
        res = self.client.get(TICKET_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_ticket_authenticated(self):
        data = {
            "cargo": 2,
            "seat": 5,
            "journey": self.journey.id,
            "order": self.order.id
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        res = self.client.post(TICKET_URL, data, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["cargo"], 2)
        self.assertEqual(res.data["seat"], 5)
        self.assertEqual(res.data["journey"], self.journey.id)
        self.assertEqual(res.data["order"], self.order.id)
