from asyncio import Task
from .models import JobPost, Proposal
from rest_framework import filters
from django.http import Http404, HttpResponse
from .serializers import JobSerializer, JobSearchSerializer, ProposalSerializer
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
    search_fields = ['sub_category']
    



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

   

class  ProposalAPIView(generics.CreateAPIView):
    serializer_class = ProposalSerializer
    look_up = 'id',
    queryset = Proposal.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data = request.data
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {
            'msg': 'Your proposal have been successfully Submitted',
            'status': status.HTTP_201_CREATED,
            'serializer' : serializer.data
        }
    
        return res
    def perform_create(self, serializer):
        try:
            task = Task.object.get(id=self.request.user.task.id)
        except Task.DoesNotExist:
            raise Http404
        if self.request.user.is_authenticated():
            serializer.save(task=task)
        serializer.save()

class UpdateJob(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = JobSerializer
    queryset = JobPost.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    
    