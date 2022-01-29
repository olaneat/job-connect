from django.urls import path
from .apiViews import (
    CreateJobPost,
    JobListAPI,
    UpdateJob,
    ProposalAPIView,
    DisplayJobById
)
app_name = 'job'

urlpatterns = [
    path('create', CreateJobPost.as_view(), name='job-posting'),
    path('list', JobListAPI.as_view(), name='job-listing'),
    path('<uuid:id>/update', UpdateJob.as_view(), name='job_post_update' ),
    path('<uuid:id>/display', DisplayJobById.as_view(), name='display-job'),
    path('submit-proposal', ProposalAPIView.as_view(), name='submit_proposal')

]