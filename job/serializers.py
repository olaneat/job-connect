
from rest_framework import serializers 
from .models import JobPost, Proposal, SaveJobs


class ProposalSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    task = serializers.CharField(source='proposal.title', read_only=True) 
    class Meta:
        model = Proposal
        fields = [
            'id',
            'proposal_description',
            'duration',
            'bid',
            'user',
            'task',
            'created_at'
        ]

  
    

class JobSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    firstname = serializers.CharField(source='user.user_profile.firstName',read_only=True) 
    surname = serializers.CharField(source='user.user_profile.surname',read_only=True)
    proposal = ProposalSerializer(many=True, read_only=True)     
    class Meta:
        model = JobPost
        fields = [
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
                    'created_on',
                    'firstname',
                    'surname'
                ]
    
    
    
    '''
    
    
    
    
    '''

'''
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
                    'location',
                    'category',
                    'sub_category',
                    'created_on'
                ]


class JobSearchSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',    read_only=True )
    class Meta:
        model = JobPost
        fields = ['user', 'id', 'title', 'description', 'budget', 'deadline']





'''


class SavedJobSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="user.id", read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = JobPost
        fields = [
            'user_id',
            'user',
            'title'
        ]