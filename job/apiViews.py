from django.db import models
from django.db.models import query
from .models import JobPost
from .serializers import JobPostSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response


class CreateJobPost(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.request.user.id
        queryset = JobPost.objects.filter(id=id)
        return queryset

    