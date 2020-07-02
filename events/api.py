from .models import Events, Tags, Categories
from rest_framework import viewsets
from .serializers import EventsSerializer, TagsSerializer, CategoriesSerializer

class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objets.all()
    serializer_class = CategoriesSerializer