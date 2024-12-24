from rest_framework import serializers
from .models import ApClass 

class ApClassSerializer(serializers.ModelSerializer):
    
    # Objects that should be declared as their string representation (__str__ method)
    subject = serializers.StringRelatedField()
    grade_level = serializers.StringRelatedField(many=True)
    benefits = serializers.StringRelatedField(many=True)
    prereqs = serializers.StringRelatedField(many=True)

    class Meta:
        model = ApClass
        fields = '__all__'
        read_only_fields = ['slug']




