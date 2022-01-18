from django.db import models
from register.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user_profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    dateOfBirth = models.DateField(blank=True,null=True)
    displayPicture = models.ImageField(upload_to='media/dp', blank=True, null=True)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    ninNumber = models.CharField(max_length=25)
    categories = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    subSkills = models.TextField()
    educationLevel = models.CharField(max_length=150)

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()