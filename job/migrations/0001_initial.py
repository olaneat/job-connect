# Generated by Django 3.2.8 on 2022-03-14 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sub_category', models.TextField()),
                ('description', models.TextField()),
                ('budget_type', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('deadline', models.DateField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('budget', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Job Post',
                'verbose_name_plural': 'Job Posts',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('duration', models.CharField(max_length=150)),
                ('proposal_description', models.TextField()),
                ('bid', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Prosposal',
                'verbose_name_plural': ' Proposals',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SaveJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('saved_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Saved Job',
                'verbose_name_plural': ' Saved Jobs',
                'ordering': ['-saved_on', 'title'],
            },
        ),
    ]
