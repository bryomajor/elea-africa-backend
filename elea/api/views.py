from django.contrib.auth.models import User
from .models import Event, Contact
from rest_framework import viewsets
from .serializers import EventSerializer, ContactSerializer

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer