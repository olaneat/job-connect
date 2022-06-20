
from rest_framework import serializers 
from .models import JobPost, Proposal, SaveJobs


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = [
            'id',
            'proposal_description',
            'duration',
            'bid',
            'created_at'
        ]

  
class ListPropalSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='user.user_profile.firstName',read_only=True) 
    surname = serializers.CharField(source='user.user_profile.surname',read_only=True)
    dp= serializers.ImageField(source="user.user_profile.displayPicture", read_only=True)
    username = serializers.CharField(source='user.username',read_only=True)
    task_title = serializers.CharField(source="task.title", read_only=True)
    class Meta:
        model = Proposal
        fields = [
            'user',
            'firstname',
            'surname',
            'task_title',
            'task',
            'id',
            'proposal_description',
            'duration',
            'bid',
            'created_at',
            'dp',
            'username'
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
                    'location',
                    'sub_category',
                    'created_on',
                    'firstname',
                    'surname'
                ]
    
    

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

class SendNotificationSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    fields = ['email']