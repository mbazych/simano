from rest_framework import serializers
from .models import Events, Tags

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"