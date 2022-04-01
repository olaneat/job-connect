from django.db import models
from register.models import CustomUser
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import cloudinary


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user_profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    dateOfBirth = models.DateField(blank=True,null=True)
    displayPicture = CloudinaryField('displayPicture')
    email = models.EmailField(blank=True, null=True)
    linkedln_url = models.CharField(max_length = 200, blank=True, null=True)
    twitter_url = models.CharField(max_length = 200, blank=True, null=True)
    countryBase = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    ninNumber = models.CharField(max_length=25, blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    subSkills = models.TextField(blank=True, null=True)
    educationLevel = models.CharField(max_length=150, blank=True, null=True)

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()

@receiver(pre_delete, sender=UserProfile)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

