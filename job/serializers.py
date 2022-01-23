from rest_framework import serializers 
from .models import JobPost

class JobSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True )
    user_id = serializers.CharField(source='user.id', read_only=True)
    
    class Meta:
        model = JobPost
        fields = ['user',
                    'user_id',
                    'id', 
                    'title', 
                    'description', 
                    'budget', 
                    'budget_type',
                    'deadline',
                    'category',
                    'sub_category']


class JobSearchSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',    read_only=True )
    class Meta:
        model = JobPost
        fields = ['user', 'id', 'title', 'description', 'budget', 'deadline']
