# Generated by Django 3.2.8 on 2022-01-17 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobpost_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='skills_required',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
