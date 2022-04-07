# Generated by Django 3.2.8 on 2022-04-07 18:49

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('displayPicture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='displayPicture')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('linkedln_url', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=200, null=True)),
                ('countryBase', models.CharField(blank=True, max_length=200, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('ninNumber', models.CharField(blank=True, max_length=25, null=True)),
                ('categories', models.CharField(blank=True, max_length=255, null=True)),
                ('skills', models.CharField(blank=True, max_length=255, null=True)),
                ('subSkills', models.TextField(blank=True, null=True)),
                ('educationLevel', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
