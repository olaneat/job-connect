from django.urls import path
from .apiViews import CreateJobPost

app_name = 'job'

urlpatterns = [
    path('posting', CreateJobPost.as_view(), name='job-posting')
]