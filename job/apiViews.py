from django.db import models
from django.db.models import query
from .models import JobPost
from rest_framework import filters
from .serializers import JobSerializer, JobSearchSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response


class CreateJobPost(generics.CreateAPIView):
    serializer_class = JobSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.request.user_id
        print(id)
        queryset = JobPost.objects.filter(id=id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
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

class JobListAPI(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = JobPost.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['skills_required']
    



class JobListByUser(generics.ListAPIView):
    serializer_class = JobSearchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user_id = self.request.user_id
        queryset = JobPost.objects.filter(id=user_id)
        return queryset

class DisplayJobById(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = JobSerializer
    permissions_classes = [permissions.IsAuthenticated]
    queryset = JobPost.objects.all()

    
   


class UpdateJob(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = JobSerializer
    queryset = JobPost.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    
    