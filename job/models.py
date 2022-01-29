from django.db import models
from register.models import CustomUser
import uuid

class JobPost(models.Model):
    id= models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, related_name='job_posting', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.TextField()
    description = models.TextField()
    budget_type = models.CharField(max_length=100)
    deadline = models.DateField(blank=True, null=True, auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    budget = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Job Post'
        ordering = ['-title']
        verbose_name_plural = 'Job Posts'

    def __str__(self) :
        return self.title



class Proposal(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user", on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    task = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='task')
    duration = models.CharField(max_length=150)
    upload = models.FileField(upload_to='media/proposal', blank=True, null=True)
    proposal_description = models.TextField()
    bid = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Prosposal'
        verbose_name_plural = ' Proposals'
        ordering = ['-created_at']

    def __str(self):
        return self.username