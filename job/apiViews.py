from .models import JobPost, Proposal, SaveJobs
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http import Http404, HttpResponse
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json

from .serializers import (JobSerializer, 
        SavedJobSerializer, 
        ProposalSerializer, 
        ListPropalSerializer,
        SendNotificationSerializer
    )
from rest_framework import generics
from rest_framework import permissions
from utils import Utils
from rest_framework import status
from rest_framework.response import Response
from register.models import CustomUser
from job import serializers


class CreateJobPost(generics.CreateAPIView):
    serializer_class = JobSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.request.user_id
        queryset = JobPost.objects.filter(id=id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
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
    queryset = JobPost.objects.all().order_by('-created_on')
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['sub_category']
    ordering = ['-created_on']



class JobListByUser(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user_id = self.request.user_id
        queryset = JobPost.objects.filter(id=user_id).order_by('-created_on')
        ordering = ['-created_on']
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


class DeleteTaskAPI(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = JobSerializer
    queryset = JobPost.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class  SubmitProposalAPIView(generics.CreateAPIView):
    serializer_class = ProposalSerializer
    look_up = 'id',
    queryset = Proposal.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


    def post(self, request, id, *args, **kwargs):
        task = get_object_or_404(JobPost, id=id)
        serializers = ProposalSerializer(data= request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(user=request.user, task=task)
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response("error", serializers.error, status=400)


class UserProposalListView(generics.ListAPIView):
    
    def  get(self, request, id ):
        queryset = Proposal.objects.filter(user=id).order_by('-created_at')
        serializer = ListPropalSerializer(queryset, many=True)
        permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListProposalsView(generics.ListAPIView):
    
    def  get(self, request, id ):
        queryset = Proposal.objects.filter(task=id).order_by('-created_at')
        serializer = ListPropalSerializer(queryset, many=True)
        permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getUserTaskList(request, id):
    if request.method == 'GET':
        tasks = JobPost.objects.filter(user_id=id)
        serializer = JobSerializer(tasks, many=True)

        res = {
            'message': 'Tasks Fetched Successfully',
            'status': status.HTTP_200_OK,
            'data': serializer.data         
        }

        return Response(res)



class ListSavedTasksAPIView(generics.ListAPIView):
    serializer_class = SavedJobSerializer
    permissions = [permissions.IsAuthenticated]
    queryset = SaveJobs.objects.all()

@api_view(['GET'])
def ListSavedJobView(request, id):
    if request.method == 'GET':
        user_id = id
        print(request.user)
        tasks = SaveJobs.objects.all()
        serializers = SavedJobSerializer()
        res = {
            'msg': 'data fetched successfully',
            'status': status.HTTP_200_OK,
            'serializer' : serializers.data
        }

        return Response(res)


class DeleteSavedJobs(generics.DestroyAPIView):
    lookup_field = 'id'
    permissions_classes = [permissions.IsAuthenticated]
    serializers = SavedJobSerializer
    queryset = SaveJobs.objects.all()


class SaveJobView(generics.CreateAPIView):
    lookup_field = 'id'
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = SavedJobSerializer
    queryset =  SaveJobs.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = SavedJobSerializer(data=request.data)
        user = request.user
        if serializer.is_valid(raise_exception=True):

            serializer.save(user=user)
            res = {
                'message': 'Job Post Successfully Saved',
                'status': status.HTTP_200_OK,
                'data': serializer.data 
            }
            return Response(res)
        else: 
            return Response('err', serializer.error, status=400)


    '''
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = {
            'message': 'Job Post Successfully Saved',
            'status': status.HTTP_200_OK,
            'data': serializer.data 
        }

        return Response(res)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    '''


class DeleteProposalView(generics.DestroyAPIView):
    lookup_field = 'id'
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer



class UpdateProposalView(generics.UpdateAPIView):
    lookup_field = 'id'
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


@api_view(['GET'])
def GetUserProposalsView(request, id):
    if request.method == 'GET':
        queryset = Proposal.objects.filter(user_id=id)
        serializer = ProposalSerializer(queryset, many=True)
        res = {
            'msg': 'Proposal List',
            'status': status.HTTP_200_OK,
            'data': serializer.data 
        }

    return Response(res)


class SendMailNotificationAPI(generics.GenericAPIView):
    serializer_class = SendNotificationSerializer
    def post(self, request):
        email = request.data['email']
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            subject = 'Proposal Accepted'
            title = request.data['title']
            body = 'Congrats', user.user_profile.firstName, user.user_profile.surname,  \
                'Your proposal for the', title,  \
                'project has been accepted'
                
            data = {
                'recieptient':user.email,
                'subject': subject,
                'body':body,
            }
            Utils.send_mail(data)

            res = {
                'msg': 'Notifcation sent successfully',
                'status': status.HTTP_200_OK,
            }
            return Response(res)



@require_POST
@csrf_exempt
def send_noification(request):
    try:
        body = request.data,
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})
        
        user_id = data['id']
        user = get_object_or_404(CustomUser, id=user_id)
        payload = {"head":data['head'], "body":data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        res = {
            'msg':'Notification Sent successfully',
            'status': status.HTTP_200_OK,
        }
        return Response(res)
    except TypeError:
        res = {
            'msg':'Error Occurs',
            'status': status.HTTP_500_BAD_REQUEST
        }
        return Response(res)