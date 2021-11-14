from django.urls import path
from .apiViews import (
    CreateJobPost,
    JobListAPI,
    UpdateJob,
    DisplayJobById
)
app_name = 'job'

urlpatterns = [
    path('posting', CreateJobPost.as_view(), name='job-posting'),
    path('list', JobListAPI.as_view(), name='job-listing'),
    path('update/<uuid:id>', UpdateJob.as_view(), name='job_post_update' ),
    path('display-by-id/<uuid:id>', DisplayJobById.as_view(), name='display-job')
]