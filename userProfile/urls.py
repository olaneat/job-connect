from django.urls import path
from .views import (
    createProfileView,
    DisplayUserList, 
    UpdateProfile, 
    UploadProfilePicture,
    RetrieveProfile,
    )


app_name = 'userProfile'
urlpatterns = [
    path('create', createProfileView.as_view(), name='create-profile'),
    path('<uuid:user_id>/update',UpdateProfile.as_view(), name="update-profile"),
    path('<uuid:user_id>/display',RetrieveProfile.as_view(), name="display-profile"),
    path('', DisplayUserList.as_view(), name='display-user-profile'),
    path('upload-image', UploadProfilePicture.as_view(), name='upload_img')    
]