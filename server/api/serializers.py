from rest_framework import serializers
from classes.models import ApClass
from events.models import Event

class ApClassSerializer(serializers.ModelSerializer):
    
    # Objects that should be declared as their string representation (__str__ method)
    subject = serializers.StringRelatedField()
    grade_level = serializers.StringRelatedField(many=True)
    prerequisite = serializers.StringRelatedField(many=True)

    class Meta:
        model = ApClass
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'