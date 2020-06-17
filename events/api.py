from .models import Events, Tags
from rest_framework import viewsets
from .serializers import EventsSerializer, TagsSerializer

class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer