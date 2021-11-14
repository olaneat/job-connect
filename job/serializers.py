from rest_framework import serializers 
from .models import JobPost

class JobSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',    read_only=True )
    class Meta:
        model = JobPost
        fields = ['user', 'id', 'title', 'description', 'budget', 'deadline']
