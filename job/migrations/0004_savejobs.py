# Generated by Django 3.2.8 on 2022-03-07 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0003_jobpost_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('saved_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_jobs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Saved Job',
                'verbose_name_plural': ' Saved Jobs',
                'ordering': ['-saved_on', 'title'],
            },
        ),
    ]
