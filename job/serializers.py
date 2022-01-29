from asyncore import read
from pyexpat import model
from rest_framework import serializers 
from .models import JobPost, Proposal

class JobSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True )
    user_id = serializers.CharField(source='user.id', read_only=True)
    
    class Meta:
        model = JobPost
        fields = [
                    'user',
                    'user_id',
                    'id', 
                    'title', 
                    'description', 
                    'budget', 
                    'budget_type',
                    'deadline',
                    'category',
                    'sub_category',
                    'created_on'
                ]


class JobSearchSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',    read_only=True )
    class Meta:
        model = JobPost
        fields = ['user', 'id', 'title', 'description', 'budget', 'deadline']



class ProposalSerializer(serializers.ModelSerializer):
    task = serializers.CharField(source='task.title', read_only=True)
    user = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Proposal
        fields = [
            'task',
            'proposal',
            'duration',
            'bid',
            'upload',
            'user',
            'created_at'
        ]