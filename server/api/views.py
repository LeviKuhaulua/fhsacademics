from rest_framework import generics
from classes.models import ApClass
from .serializers import ApClassSerializer

class ApClassList(generics.ListAPIView):
    queryset = ApClass.objects.all().select_related('subject').prefetch_related('grade_level', 'benefits', 'prereqs')
    serializer_class = ApClassSerializer


class ApClassDetail(generics.RetrieveAPIView):
    queryset = ApClass.objects.all().select_related('subject').prefetch_related('grade_level', 'benefits', 'prereqs')
    serializer_class = ApClassSerializer
    lookup_field = 'slug'