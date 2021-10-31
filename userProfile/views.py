from register import permissions, serializers
from register.models import CustomUser
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.parsers import  MultiPartParser, FormParser
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response



class createProfileView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class   = UserProfileSerializer
    permission_classes= [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance = request.user.user_profile 
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status =status.HTTP_201_CREATED,
            headers= headers
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DisplayUserList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UpdateProfile(generics.UpdateAPIView):
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()


class RetrieveProfile(generics.RetrieveAPIView):
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    