from rest_framework import generics
from classes.models import ApClass
from events.models import Event
from .serializers import ApClassSerializer, EventSerializer

class ApClassList(generics.ListAPIView):
    queryset = ApClass.objects.all().select_related('subject').prefetch_related('grade_level', 'benefits', 'prereqs')
    serializer_class = ApClassSerializer


class ApClassDetail(generics.RetrieveAPIView):
    queryset = ApClass.objects.all().select_related('subject').prefetch_related('grade_level', 'benefits', 'prereqs')
    serializer_class = ApClassSerializer
    lookup_field = 'slug'

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'