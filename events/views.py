from rest_framework import generics
from .models import Events
from .serializers import EventsSerializer

# class ListEventsView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Events.objects.all()
#     serializer_class = EventsSerializer