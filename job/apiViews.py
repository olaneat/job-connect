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
        id = self.request.user_id
        print(id)
        queryset = JobPost.objects.filter(id=id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance = request.user.job_posting.first()
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = {
            'message': 'Job Post Successfully Created',
            'status': status.HTTP_201_CREATED,
            'serializer': serializer.data 
        }

        return Response(res)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
        