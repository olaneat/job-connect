from unicodedata import name
from django.urls import path
from .apiViews import (
    CreateJobPost,
    JobListAPI,
    UpdateJob,
    SubmitProposalAPIView,
    DisplayJobById,
    DeleteTaskAPI,
    ListSavedJobView,
    DeleteSavedJobs,
    SaveJobView,
    ListProposalsView
)
from . import apiViews
app_name = 'job'

urlpatterns = [
    path('create', CreateJobPost.as_view(), name='job-posting'),
    path('list', JobListAPI.as_view(), name='job-listing'),
    path('<uuid:id>/update', UpdateJob.as_view(), name='job_post_update' ),
    path('<uuid:id>/display', DisplayJobById.as_view(), name='display-job'),
    path('<uuid:id>/user-task-list', apiViews.getUserTaskList, name="user-task-list"),
    path('<uuid:id>/delete', DeleteTaskAPI.as_view(), name="delete-task"),
    path('<uuid:id>/submit_proposal', SubmitProposalAPIView.as_view(), name="make-proposal"),
    path('<uuid:id>/display_proposals', ListProposalsView.as_view(), name="display-proposal"),
    path('saved-task-list', ListSavedJobView, name='display-saved-task'),
    path('save-task', SaveJobView.as_view(), name='saved-job')

]