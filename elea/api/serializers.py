from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Contact, EventImage

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['image']

class EventSerializer(serializers.ModelSerializer):
    eventimages = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'location', 'date', 'description', 'thumbnail', 'eventimages']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['fullname', 'useremail', 'usermessage']