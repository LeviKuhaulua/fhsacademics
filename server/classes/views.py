from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from .models import ApClass
from .serializers import ApClassSerializer

# Create your views here.
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def listAps(request):
    aps = ApClass.objects.all().select_related('subject').prefetch_related('grade_level', 'benefits', 'prereqs')
    serializer = ApClassSerializer(aps, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def apClassDetail(request, class_name):

    try: 
        ap = ApClass.objects.get(slug=class_name)
        serializer = ApClassSerializer(ap)
        return Response(serializer.data)
    except ApClass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    