from asyncore import read
from pyexpat import model
from rest_framework import serializers 
from .models import JobPost, Proposal

class JobSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True )
    user_id = serializers.CharField(source='user.id', read_only=True)
    proposal = serializers.StringRelatedField(many=True, read_only=True)     
    class Meta:
        model = JobPost
        fields = [
                    'user',
                    'user_id',
                    'id', 
                    'proposal',
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
    task = JobSerializer(many=True, read_only=True)
    user = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Proposal
        fields = [
            'task',
            'id',
            'proposal_description',
            'duration',
            'bid',
            'upload',
            'user',
            'created_at'
        ]