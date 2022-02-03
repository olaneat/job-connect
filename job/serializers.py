from asyncio import tasks
from asyncore import read
from pyexpat import model
from rest_framework import serializers 
from .models import JobPost, Proposal


class ProposalSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    
    class Meta:
        model = Proposal
        fields = [
            'id',
            'proposal_description',
            'duration',
            'bid',
            'user',
            'created_at'
        ]


    

class JobSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True )
    user_id = serializers.CharField(source='user.id', read_only=True)
    task = ProposalSerializer(many=True, read_only=True)     
    class Meta:
        model = JobPost
        fields = [
                    'user',
                    'user_id',
                    'id', 
                    'task',
                    'title', 
                    'description', 
                    'budget', 
                    'budget_type',
                    'deadline',
                    'category',
                    'sub_category',
                    'created_on'
                ]

    '''
    def create(self, validated_data):
        if 'proposals' in validated_data:
            proposals_data = validated_data.pop('proposals')
        else:
            proposal = Proposal.objects.create(**validated_data)
        task = JobPost.objects.update_or_create(
            proposal=proposal, defaults=validated_data
        )
        return task


    
    
    
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
                    'category',
                    'sub_category',
                    'created_on'
                ]


'''

class JobSearchSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',    read_only=True )
    class Meta:
        model = JobPost
        fields = ['user', 'id', 'title', 'description', 'budget', 'deadline']



