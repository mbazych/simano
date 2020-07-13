from rest_framework import serializers
from .models import Events, Tags, City, Country, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class EventsSerializer(serializers.ModelSerializer):
    #author = serializers.(lookup_field='author.username')
    #participants = serializers.Field(source='participants.name')
    
    class Meta:
        model = Events
        fields = "__all__"

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

