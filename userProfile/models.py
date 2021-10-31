from django.db import models
from register.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user_profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True,null=True)
    display_picture = models.ImageField(upload_to='media/dp')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    n_i_n = models.CharField(max_length=25)
    skills = models.TextField()
    education_level = models.CharField(max_length=150)

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()