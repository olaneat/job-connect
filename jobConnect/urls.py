from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('register.urls', namespace='account')),
    path('profile/', include('userProfile.urls', namespace='userProfile')),
    path('job/', include('job.urls', namespace='job'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

