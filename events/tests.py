from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Events
from .serializers import EventsSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_event(title="", author=""):
        if title != "" and author != "":
            Events.objects.create(title=title, author=author)

    def setUp(self):
        self.create_event("Cooking lessons", "Amanda Daymond")
        self.create_event("DevOps introduction", "Paweł Jackowski")
        self.create_event("Making fried chicken in 5 minutes", "Luiziano Amore")
        self.create_event("Get good at managing business", "Antoni Pertocci")

class GetAllEventsTest(BaseViewTest):

    def test_get_all_events(self):
        """
        This test ensures that all events added in the setUp method 
        exist when we make a GET request to the events/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("events-all", kwargs={"version": "v1"})
        )
        # fetch data from db
        expected = Events.objects.all()
        serialized = EventsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
