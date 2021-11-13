from django.db import models
from register.models import CustomUser

class JobPost(models.Model):
    user = models.ForeignKey(CustomUser, related_name='job_posting', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(blank=True, null=True, auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    budget = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Job Post'
        ordering = ['-title']
        verbose_name_plural = 'Job Posts'

    def __str__(self) :
        return self.title


