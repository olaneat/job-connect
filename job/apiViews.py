from asyncio import Task, tasks
import re
from trace import Trace
from register.models import CustomUser
from .models import JobPost, Proposal
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
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


class UpdateJob(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = JobSerializer
    queryset = JobPost.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    

class  SubmitProposalAPIView(generics.CreateAPIView):
    serializer_class = ProposalSerializer
    look_up = 'id',
    queryset = Proposal.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    
    

@api_view(['GET'])
def getUserTaskList(request, id):
    if request.method == 'GET':
        tasks = JobPost.objects.filter(user_id=id)
        serializer = JobSerializer(tasks, many=True)

        res = {
            'message': '',
            'status': status.HTTP_200_OK,
            'data': serializer.data         
        }

        return Response(res)


'''
   
@api_view(['GET', 'POST'])
def submitProposalAPIView(request, id, **validated_data):
    task = get_object_or_404(JobPost, id=id)
    print(id)
    if request.method == 'POST':
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid(**validated_data):
            proposal = serializer.save(id=id)
            proposal.task = task
            proposal.save()
            res = {
                'message': 'Proposal Submitted Successfully',
                'status': status.HTTP_200_OK,
                serializer : serializer.data
            }
            return Response(res)
    else:
        serializer = ProposalSerializer()
    return Response({'request':request, 'serializer': serializer})

''' 
        
    
    