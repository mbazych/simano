from .models import Events, Tags, City, Country, Category
from rest_framework import viewsets
from .serializers import EventsSerializer, TagsSerializer, CitySerializer, CountrySerializer, CategorySerializer
from rest_framework import  viewsets, permissions

class EventsViewset(viewsets.ModelViewSet):
    
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]